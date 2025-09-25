from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('login_user/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('verify_user/', views.verify_code, name='verify_user'),
    path('verify_user_page/', views.verify_code_page, name='verify_user_page'),
    path("new/", views.new_diary, name="new_diary"),
    path("view/<int:diary_id>/", views.view_diary, name="view_diary"),
    path("delete/<int:diary_id>/", views.delete_diary, name="delete_diary"),
    path('logout/', views.logout_view, name='logout'),
]