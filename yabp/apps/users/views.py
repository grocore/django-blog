from django.shortcuts import render


def user_profile(request):
    context = {'user': 'World', 'title': 'Profile'}
    return render(request, 'user_profile.html', context)
