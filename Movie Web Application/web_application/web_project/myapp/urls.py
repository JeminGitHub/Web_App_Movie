from django.urls import path
from . import views

app_name = 'myapp'  # ---> NameSpace
urlpatterns = [

    path('', views.index, name='home'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('login/',views.login,name='login'),
    # path('sign',views.sign,name='sign'),
    path('add/',views.add_movies,name='add_movies'),
    path('update/<int:id>',views.update,name='updates'),
    path('movies',views.movies,name='movies'),
    path('mail',views.profiles,name='profiles'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('user',views.user,name='user'),


]
