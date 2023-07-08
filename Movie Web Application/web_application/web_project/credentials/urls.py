from django.urls import path
from . import views




app_name = 'credentials'  # ---> NameSpace




urlpatterns = [

    path('', views.user_movies, name='user_movies'),
    # Other URL patterns for your second app

    path("signup", views.register_request, name="signup"),
    path("signin", views.login_request, name="signin")
]

