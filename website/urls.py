from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show_details/(?P<item_id>\d+)/$', views.show_details, name='show_details'),

]