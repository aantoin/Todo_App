# Create your views here.
from typing import Any

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from todo_app.checklists.models import Checklist, ChecklistItem

from .serializers import ChecklistItemSerializer, ChecklistSerializer


# Create your views here.
class ChecklistViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Checklist.objects.none()
    serializer_class = ChecklistSerializer

    def get_queryset(self):
        return self.request.user.checklist_set.all()


class ChecklistItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ChecklistItem.objects.none()
    serializer_class = ChecklistItemSerializer

    def get_queryset(self):
        return ChecklistItem.objects.filter(
            checklist=self.kwargs["checklist_pk"], checklist__owner=self.request.user
        ).all()

    def get_serializer(self, *args: Any, **kwargs: Any):
        if "data" in kwargs:
            kwargs["data"]["checklist"] = self.kwargs["checklist_pk"]
        return super().get_serializer(*args, **kwargs)
