from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from .forms import CustomUserCreationForm

User = get_user_model()

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_secure():
            protocol = 'https'
        else:
            protocol = 'http'
        current_site = get_current_site(self.request)
        mail_subject = 'Activación de cuenta.'
        message = render_to_string('account/activation_email.html', {
            'user': self.object,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(self.object.pk)),
            'token': default_token_generator.make_token(self.object),
            'protocol': protocol,
        })
        try:
            send_mail(mail_subject, message, 'pcychips@gmail.com', ['edgaytanc@gmail.com'])
        except Exception as e:
            print(e)
        return response


class UserUpdateView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'account/update.html'
    success_url = reverse_lazy('account')

    def get_object(self):
        return self.request.user
    


class UserDeleteView(DeleteView):
    model = User
    template_name = 'account/delete.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user
    
    
def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_activated = True
        user.save()
        return redirect('login')
    else:
        return render(request, 'account/activation_invalid.html')
