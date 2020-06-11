from django.shortcuts import render, redirect
from .forms import CreateUserForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    else:
        form = EditProfileForm(instance=request.user.profile)
    context = {'form': form, 'title': 'Profile'}
    return render(request, 'user_profile.html', context)


def user_create(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    else:
        form = CreateUserForm()
    context = {
        'form': form,
        'title': 'Sign Up'
    }
    return render(request, 'user_create.html', context)
