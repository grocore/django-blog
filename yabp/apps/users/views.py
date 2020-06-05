from django.shortcuts import render


def user_profile(request):
    context = {'user': 'World'}
    return render(request, 'user_profile.html', context)
