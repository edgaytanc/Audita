from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
from . forms import CustomUserEditForm
from users.decorators import user_is_superuser, auditor_required

@user_is_superuser

def admin_dashboard_view(request):
    return render(request, 'dashboard/admin_dashboard.html')

@user_is_superuser

def list_users(request):
    users = CustomUser.objects.all()
    return render(request, 'dashboard/users_list_dashboard.html', {'users': users})

@user_is_superuser

def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = CustomUserEditForm(instance=user)
    return render(request, 'dashboard/edit_user.html', {'form': form})

@user_is_superuser

def delete_user(request, user_id):
    user=get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('list_users')