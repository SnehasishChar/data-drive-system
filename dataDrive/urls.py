from django.urls import path

from dataDrive import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.register, name='register'),
    path('view_folder/<_id>', views.view_folder, name='view_folder'),
]
