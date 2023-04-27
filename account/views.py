from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import RegistrationFrom
from .token import account_activation_token

def account_register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        registerForm = RegistrationFrom(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            # setup email
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('account/registration/account_acctivation_email.html', 
                                       {'user': user, 
                                        'domain': current_site.domain, 
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)), 
                                        'token': account_activation_token.make_token(user),})
            user.email_user(subject=subject, message=message)
    else:
        registerForm = RegistrationFrom()
    return render(request, 'account/registration/register.html', {'form':registerForm})