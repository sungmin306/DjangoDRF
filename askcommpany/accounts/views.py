from typing_extensions import Required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# class ProfileView(LoginRequiredMixin, TemplateView):
#     template_name: 'accounts/profile.html'

# profile = ProfileView.as_view()