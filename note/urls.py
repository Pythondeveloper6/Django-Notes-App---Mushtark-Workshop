from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.notes , name='notes'),
    # url(r'^(?P<id>\d+)$', views.detail),

    url(r'^(?P<slug>[-\w]+)/$', views.detail , name='note_detail'),

]
