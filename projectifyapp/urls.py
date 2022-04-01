from django.urls import path, include

from rest_framework.routers import DefaultRouter

from projectifyapp.views import ProjectView, OperationalUserView

router = DefaultRouter()

router.register('project', ProjectView)
router.register('operational-user', OperationalUserView)

urlpatterns = [
    path('', include(router.urls)),
]
