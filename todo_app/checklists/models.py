# Create your models here.
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Checklist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(null=False)

    class ItemCompleteAction(models.TextChoices):
        DELETE = "DEL", _("Delete")
        STRIKE = "STR", _("Strike")
        CHECK = "CHE", _("Check")

    item_complete_action = models.CharField(
        max_length=3,
        choices=ItemCompleteAction.choices,
        default=ItemCompleteAction.CHECK,
    )
    hide_completed = models.BooleanField(default=False)
    hide_until_due = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_order = self.order

    def save(self, *args, **kwargs):
        checklists = []
        if self.order != self.__original_order or self._state.adding:
            checklists = Checklist.objects.filter(owner=self.owner).all()
            self.order = max(
                0, min(max((x.order for x in checklists), default=-1) + int(self._state.adding), self.order)
            )
            if self.order > self.__original_order:
                checklists = [x for x in checklists if x.order <= self.order and x.order > self.__original_order]
                for checklist in checklists:
                    checklist.order = checklist.order + 1
            else:
                checklists = [
                    x
                    for x in checklists
                    if x.order >= self.order and (self._state.adding or x.order < self.__original_order)
                ]
                for checklist in checklists:
                    checklist.order = checklist.order - 1
            Checklist.objects.bulk_update(checklists, ["order"])
        try:
            super().save(*args, **kwargs)
        except Exception:
            if checklists:
                for checklist in checklists:
                    checklist.order = checklist.__original_order
                Checklist.objects.bulk_update(checklists, ["order"])
            raise
        self.__original_order = self.order


class ChecklistItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name="items")
    content = models.TextField()
    completed = models.BooleanField(default=False)
    order_left = models.IntegerField()
    order_right = models.IntegerField()

    def delete(self, *args, **kwargs):
        print("Delete", self.id)
        super().delete(*args, **kwargs)
        ChecklistItem.objects.filter(
            checklist=self.checklist_id, order_left__gt=self.order_left, order_left__lt=self.order_right
        ).delete()
        items = list(ChecklistItem.objects.filter(checklist=self.checklist_id, order_left__gt=self.order_left))
        for i in range(len(items)):
            items[i].order_left = items[i].order_left - (self.order_right - self.order_left + 1)
            items[i].order_right = items[i].order_right - (self.order_right - self.order_left + 1)
        ChecklistItem.objects.bulk_update(items, ["order_left", "order_right"])

    def save(self, *args, **kwargs):
        items = ChecklistItem.objects.filter(checklist=self.checklist_id).all()
        order_max = max((x.order_right for x in items), default=-1)
        # New Item
        if self._state.adding:
            self.order_left = order_max + 1
            self.order_right = self.order_left + 1
        # Existing Item
        else:
            old_item = next(filter(lambda x: x.id == self.id, items), None)
            if old_item:
                old_left = old_item.order_left
                old_right = old_item.order_right
                # Item order is changed
                if old_left != self.order_left:
                    if self.order_left < 0 or self.order_left >= order_max:
                        self.order_left = order_max + 1
                    difference = self.order_left - old_left
                    size = old_right - old_left + 1
                    # New location is right of current location
                    if self.order_left > old_right + 1:
                        for item in items:
                            if item.order_left >= old_left:
                                # Item to the right of block
                                if item.order_left > old_right:
                                    if item.order_left < self.left:
                                        item.order_left = item.order_left - size
                                    if item.order_right < self.left:
                                        item.order_right = item.order_right - size
                                # Self or sub-item
                                else:
                                    difference = self.order_left - old_right - 1
                                    item.order_left = item.order_left + difference
                                    item.order_right = item.order_right + difference
                    # New location is left of current location
                    if self.order_left < old_left:
                        for item in items:
                            if item.order_left >= old_left and item.order_left < old_right:
                                item.order_left = item.order_left - (old_left - self.order_left)
                                item.order_right = item.order_right - (old_left - self.order_left)
                            elif item.order_left < old_left and item.order_left >= self.order_left:
                                item.order_left = item.order_left + size
                            elif item.order_right < old_left and item.order_right >= self.order_left:
                                item.order_right = item.order_right + size
                    self.order_left = old_item.order_left
                    self.order_right = old_item.order_right
                    ChecklistItem.objects.bulk_update(items, ["order_left", "order_right"])
        super().save(*args, **kwargs)
