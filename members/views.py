from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your views here.
from django.views.generic import DetailView

from blog.models import Profile, Comment
from members.forms import SignUpForm, EditProfileForm, PasswordChangeForm1, ProfilePageForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangeForm1
    template_name='registration/changepassword.html'
    success_url = reverse_lazy('password_changed_success')

def password_success(request):
    return render(request, 'registration/changepasswordsuccess.html')

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_user_profile.html'
    fields = ['bio', 'photo', 'website_url', 'github_url']

class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

