from django.db.models import QuerySet
from rest_framework import serializers

from todo_app.checklists.models import Checklist, ChecklistItem


class ChecklistOrderDefault:
    requires_context = True

    def __call__(self, field):
        return Checklist.objects.filter(owner=field.context["request"].user).count()


class ChecklistSerializer(serializers.ModelSerializer[Checklist]):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order = serializers.IntegerField(default=ChecklistOrderDefault())

    def validate(self, data):
        num_checklists = Checklist.objects.filter(owner=data["owner"]).count()
        if data["order"] < 0 or data["order"] < num_checklists + int("id" in data):
            raise serializers.ValidationError("Invalid order number")
        return data

    class Meta:
        model = Checklist
        read_only_fields = ["owner"]
        fields = [
            "id",
            "owner",
            "name",
            "date_created",
            "order",
            "item_complete_action",
            "hide_completed",
            "hide_until_due",
        ]


class ChecklistPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self) -> QuerySet:
        request = self.context.get("request", None)
        queryset = super().get_queryset()
        if not request or not request.user.is_authenticated or not queryset:
            return None
        return queryset.filter(owner=request.user)


class ChecklistItemSerializer(serializers.ModelSerializer[ChecklistItem]):
    checklist = ChecklistPrimaryKeyRelatedField(many=False, queryset=Checklist.objects.all())
    order_left = serializers.IntegerField(required=False)
    order_right = serializers.IntegerField(read_only=True)

    class Meta:
        model = ChecklistItem
        fields = [
            "id",
            "checklist",
            "content",
            "completed",
            "order_left",
            "order_right",
        ]
