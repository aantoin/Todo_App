from django.conf import settings
from django.urls import include, path
from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter, SimpleRouter

from todo_app.checklists.api.views import ChecklistItemViewSet, ChecklistViewSet
from todo_app.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("checklists", ChecklistViewSet)
checklists_router = NestedSimpleRouter(router, r"checklists", lookup="checklist")
checklists_router.register(r"items", ChecklistItemViewSet, basename="checklist-items")

app_name = "api"
urlpatterns = (
    router.urls
    + checklists_router.urls
    + [
        path("auth/", include("dj_rest_auth.urls")),
        path("auth/registration/", include("dj_rest_auth.registration.urls")),
    ]
)
