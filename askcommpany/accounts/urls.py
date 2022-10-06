from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
#path('<int:pk>/',view.post_detail)
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('profile/', views.profile, name = 'profile'),
]
