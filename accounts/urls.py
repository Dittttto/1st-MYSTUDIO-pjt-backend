from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.change_password, name='change_password'),
    path('<int:user_id>/update/',views.update_profile,name = 'update_profile'),
    path('<int:user_id>/',views.profile,name = 'profile'),
    path('<int:user_id>/follow/',views.follow,name = 'follow'),
]