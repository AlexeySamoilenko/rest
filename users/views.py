from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, CustomUserForm


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            user_form = CustomUserForm(request.POST)

            if form.is_valid() and user_form.is_valid():
                form.save()
                user_name = form.cleaned_data['username']
                user_form.save(user_name)
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/accounts')
        else:
            form = SignUpForm()
            user_form = CustomUserForm()

        return render(request, 'accounts/signup.html', {'form': form, 'user_form': user_form})
    else:
        return redirect('/accounts')


@login_required
def user(request):
    return render(request, "accounts/user.html")


