from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, CustomUserCreationForm, UserEditForm, ProfileEditForm
from .models import Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('welcome')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        new_user = form.save()
        Profile.objects.create(user=new_user)
        return super(SignUpView, self).form_valid(form)


def welcome(request):
    context = {}
    return render(request, 'registration/welcome.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    return render(request, 'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
