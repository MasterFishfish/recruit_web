from django.conf.urls import url
from .views import UserShow, ChangePassword, index, personalpage
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^personal/', personalpage, name="personal"),
    url(r'^login/', UserShow.as_view()),
    url(r'^password/', ChangePassword.as_view()),
]
