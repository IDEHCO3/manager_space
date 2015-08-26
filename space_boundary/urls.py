from django.conf.urls import url
import views

urlpatterns = (
    url(r'^$', views.SpaceBoundariesList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/', views.SpaceBoundariesDetail.as_view(), name='detail')
)