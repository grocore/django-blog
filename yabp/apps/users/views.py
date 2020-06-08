from django.shortcuts import render, redirect
from .forms import CreateUserForm


def user_profile(request):
    context = {'user': 'World', 'title': 'Profile'}
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
        'form': form
    }
    return render(request, 'user_create.html', context)
