from django.urls import path
from members.views import UserRegisterView, UserEditView, password_success, \
    PasswordsChangeView, ShowProfileView, EditProfileView, CreateProfileView
from django.contrib.auth import views as authview

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('eidt_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', password_success, name='password_changed_success'),
    path('<int:pk>/profile/', ShowProfileView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile/', EditProfileView.as_view(), name='edit_profile_page'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile_page'),
]
