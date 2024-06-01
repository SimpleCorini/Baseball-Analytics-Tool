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
            return redirect("/profile_create")
        else:
            return redirect("/analysis")
    else:   
        print("is_authenticated : false")
        return render(request, "analysis/analysis.html")

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
    return render(request, 'users/profileForm.html', {'form': form})

@login_required
def update_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profileForm.html', {'form': form})
