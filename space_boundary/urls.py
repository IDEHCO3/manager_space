from django.conf.urls import url
import views

urlpatterns = (
    url(r'^(?P<state_level>[^/]+)/$', views.SpaceBoundariesList.as_view(), name='list_state'),
    url(r'^(?P<state_level>[^/]+)/(?P<state_name>[^/]+)/$', views.SpaceBoundariesList.as_view(), name='list_state_one'),
    url(r'^(?P<state_level>[^/]+)/(?P<state_name>[^/]+)/(?P<municipio_level>[^/]+)/', views.SpaceBoundariesList.as_view(), name='list_mucipios'),
    url(r'^(?P<state_level>[^/]+)/(?P<state_name>[^/]+)/(?P<municipio_level>[^/]+)/(?P<municipio_name>[^/]+)/', views.SpaceBoundariesList.as_view(), name='list_mucipios'),
)