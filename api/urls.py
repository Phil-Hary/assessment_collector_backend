from django.urls import include, path
from rest_framework import routers

from api.views import FormResposeViewSet, FormDetailViewSet, FormApiView

router = routers.DefaultRouter()
router.register(r'(?P<form_name>[a-zA-Z0-9_-]+)', FormResposeViewSet, basename="form_response")
router.register(r'(?P<form_name>[a-zA-Z0-9_-]+)', FormDetailViewSet, basename="form_detail")

urlpatterns = [
    path('', include(router.urls)),
    path("forms/", FormApiView.as_view(), name='forms'),
]