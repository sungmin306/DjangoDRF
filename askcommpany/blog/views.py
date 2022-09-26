from django.shortcuts import render
from.models import Post
from rest_framework import generics
from . serializers import PostSerializer
# Create your views here.

def post_List(request):
    qs= Post.objects.all()
    context = {'post_list':qs}
    print(context)
    return render(request,'blog/post_list.html',context)
    # render 함수는 request, templates, 사전형 객체(dic)를 전달한다.

class ListPost(generics.ListCreateAPIView): #
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
