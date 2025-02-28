from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm, UserRegistrationForm,UpdateProfileForm,UpdateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def register(request):
    user_form = UserRegistrationForm()

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            cf = user_form.cleaned_data

            email = cf['email']
            password = cf['password']
            password2 = cf['password2']

            if User.objects.filter(email=email).exists():
                messages.error(request, 'User with that email account already exists')
            elif password != password2:
                messages.error(request, 'Passwords don\'t match')
            else:
                new_user = User.objects.create_user(
                    first_name=cf['first_name'],
                    last_name=cf['last_name'],
                    username=email,
                    password=password
                )
                Profile.objects.create(user=new_user)
                return render(request, 'accounts/register_done.html', {'new_user': new_user})

    return render(request, 'accounts/register.html', {'user_form': user_form})

def user_login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            cf = form.cleaned_data  
            try:
                user_record = User.objects.get(email=cf['email'])
            except User.DoesNotExist:
                user_record = None

            if user_record:
                user = authenticate(request, username=user_record.username, password=cf['password'])

                if user is not None:
                    login(request, user)
                    return redirect('listings:product_list')
                messages.error(request, 'Incorrect email / password')

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        user = User.objects.filter(email=email).exclude(id=request.user.id).first()

        if user:
            messages.error(request, 'User with the given email already exists.')
            return redirect('profile')

        user_form = UpdateUserForm(instance=request.user, data=request.POST)
        profile_form = UpdateProfileForm(instance=request.user.profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
