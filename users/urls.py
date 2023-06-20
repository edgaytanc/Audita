from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/', views.UserUpdateView.as_view(), name='my_account'),
    path('account/delete', views.UserDeleteView.as_view(), name='delete_account'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),
    # Reseteo de password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),

]
