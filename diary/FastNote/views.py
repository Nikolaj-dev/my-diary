from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.models import User


class AllUserNotes(LoginRequiredMixin, ListView):
    model = User
    template_name = 'FastNote/home.html'
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super(AllUserNotes, self).get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(username=self.request.user)
        return context


class CustomLoginView(LoginView):
    template_name = 'FastNote/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('notes')

