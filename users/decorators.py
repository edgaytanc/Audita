from functools import wraps
from django.http import HttpResponseForbidden

def user_is_superuser(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("No tienes permiso para acceder a esta pagina")
    return wrap

def auditor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == CustomUser.AUDITOR:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acceso solo permitido para auditores.")
    return _wrapped_view

def supervisor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == CustomUser.SUPERVISOR:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acceso solo permitido para supervisores.")
    return _wrapped_view

def jefe_auditoria_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == CustomUser.JEFE_AUDITORIA:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Acceso solo permitido para jefes de auditoría.")
    return _wrapped_view