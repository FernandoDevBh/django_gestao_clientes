from django.urls import path
from .views import home, my_logout, HomePageView


urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="logout"),
    path('home2/', HomePageView.as_view()),
]