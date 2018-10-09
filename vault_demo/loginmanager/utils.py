from django.http import HttpResponseRedirect
from django.core.handlers.wsgi import WSGIRequest

def login_required(f):
    def wrapper(*args, **kwargs):
        request = None
        for arg in args:
            if isinstance(arg, WSGIRequest):
                request = arg
                break

        if 'login' not in  request.session or not request.session['login']:
            return HttpResponseRedirect("/vault/")
        return f(*args, **kwargs)
    return wrapper

def logout_view(request):
    return HttpResponseRedirect("/vault/")