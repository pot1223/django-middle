from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def sign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
        form.is_valid()
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {
            'form': form,
        })


@login_required
def profile(request):
    return render(request, 'account/profile.html')
