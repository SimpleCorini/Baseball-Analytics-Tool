from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

def home(request):
    if request.user.is_authenticated:
        profile, created = Profile.objects.get_or_create(user=request.user)
        print("is_authenticated : true", profile.nickname, profile.favorite_team)
        if profile.nickname == "" or profile.favorite_team == "":
            return redirect("/profileForm")
        else:
            return render(request, "main.html")
    else:
        print("is_authenticated : false")
        return render(request, "home.html")

LOGIN_REDIRECT_URL = '/'

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def set_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if profile.nickname and profile.nickname.strip():
        return redirect("/")

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profileForm.html', {'form': form})
