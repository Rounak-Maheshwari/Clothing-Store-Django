from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='account-register'),
    path('login/', views.login_view, name='account-login'),
    path('logout/', views.logout_view, name='account-logout'),
    path('forgot-password/', views.forgot_password, name='account-forgot'),
    path('profile/', views.profile_view, name='account-profile'),
    path('profile/addresses', views.all_addresses, name='account-profile-address'),
    path('profile/add-new-address', views.add_new_address, name='account-profile-add_address'),
    path('profile/edit-address/<int:id>', views.edit_address, name='account-profile-edit_address'),
    path('profile/delete-address/<int:id>', views.delete_address, name='account-profile-delete_address'),
]