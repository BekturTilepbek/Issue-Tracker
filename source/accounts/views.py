from django.contrib.auth import login, get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms import RegistrationForm

User = get_user_model()


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration.html"
    model = User

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:projects')
        return next_url
