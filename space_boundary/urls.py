from django.conf.urls import url
import views

urlpatterns = (
    url(r'^(?P<dynamic_url>.*)/', views.SpaceBoundariesList.as_view()),
)