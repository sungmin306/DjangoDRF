#urls.py까지 만드는데 app을 만드는 거라고 할 수 있다.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_list)

]

