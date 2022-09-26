#urls.py까지 만드는데 app을 만드는 거라고 할 수 있다.
from . import views
from django.urls import path
urlpatterns = [
    #path('',views.post_List, name='post_List')
    path('', views.ListPost.as_view()),
    path('<int:pk>/',views.DetailPost.as_view()),
]

