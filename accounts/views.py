from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib import messages

def user_login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            cf = form.cleaned_data  # Use `cf = form.cleaned_data`, not `cf = form.cleaned_data()`
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

    # Always return a response
    return render(request, 'accounts/login.html', {'form': form})
