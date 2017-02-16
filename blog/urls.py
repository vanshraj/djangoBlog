from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$', views.post_title, name='post_title'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]