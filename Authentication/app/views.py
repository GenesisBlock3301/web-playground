from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SignUpForm, LoginForm, UserEditForm
from django.contrib.auth import login, authenticate, logout as dj_logout
from .models import Profile


class RegisterView(View):
    def get(self, request):
        form = SignUpForm
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login-user')
        return render(request, 'auth/register.html', {'form': form,'status': "Credential is not valid"})


class LoginView(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            # print(user)
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'auth/login.html', {'form': form, 'status': "Your password or username is incorrect"})


def user_logout(request):
    dj_logout(request)
    return redirect('login-user')


class HomeView(View):

    def get(self, request):
        user = request.user
        print("User", user)
        if user.is_authenticated:
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                profile = Profile.objects.create(user=user, first_name='', last_name='', degree='', description='',
                                                 age='')

            form = UserEditForm(initial={
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'degree': profile.degree,
                'description': profile.description,
                'age': profile.age
            })
            return render(request, 'Home.html', {'profile': profile, 'form': form})
        else:
            return redirect('login-user')

    def post(self, request):
        form = UserEditForm(data=request.POST or None)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.first_name = request.POST['first_name']
            profile.last_name = request.POST['last_name']
            profile.degree = request.POST['degree']
            profile.description = request.POST['description']
            profile.age = request.POST['age']
            profile.save()
            return redirect('home')
