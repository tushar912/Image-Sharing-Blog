from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ProfileForm, RegistrationForm
from .models import UserProfile

User = get_user_model()

def register(request):
    
    if request.user.is_authenticated:
        return redirect(reverse('chat:home'))


    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # Process POSTed Form data
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1']
                                    )
            # authenticate and log user in, then redirect to newsFeeds
            login(request, new_user)
            return redirect(reverse('chat:home'))

    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

