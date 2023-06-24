from django.shortcuts import redirect
from functools import wraps

def entidad_requerida(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'entidad_seleccionada_id' not in request.session:
            # Redirige a la página de selección de entidad si no se ha seleccionado ninguna entidad
            return redirect('seleccionar_entidad')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
