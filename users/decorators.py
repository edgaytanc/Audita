from django.http import HttpResponseForbidden

def user_is_superuser(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("No tienes permiso para acceder a esta pagina")
    return wrap