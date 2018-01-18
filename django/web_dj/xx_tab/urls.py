from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^index/$',views.index),
    url(r'^list/$', views.get_xxtabs),
    url(r'^list/add/$', views.add_xxtabs_form),
    url(r'^list/add/ok/$', views.add_xxtabs),
    url(r'^list/del/$', views.del_xxtabs_form),
    url(r'^list/del/ok/$', views.del_xxtabs),
]
