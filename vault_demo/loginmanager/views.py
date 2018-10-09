from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from .ldap_auth import verify_with_ad
from .forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    error_template_name = 'invalid_input.html'

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        context = {
            'form_class': form_class
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            verification, message = verify_with_ad(username, password)

            if (verification):
                request.session['username'] = username
                request.session['login'] = True
                request.session.set_expiry(900)
                return HttpResponseRedirect("/vault/landing")
            else:
                context = {
                    'form_class': form_class,
                    'invalid': True
                }
                return render(request, self.template_name, context=context, status=401)
        else:
            return render(request, self.error_template_name, status=400)