#from email import message
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.


#post_list = ListView.as_view(model=Post) # 아래 def Post_list에서 if 문을 제외한 나머지 기능을 한줄로 구현 가능


def Post_list(request):
    qs = Post.objects.all()
    #print('전체 다 가져온 qs'+qs)
    q=request.GET.get('q','')
    if q: # q라는 검색어가 존재하면
        qs = qs.filter(message__icontains=q) # 검색어가 존재하면 가져온다는 의미 icontains에 대해서 공부해보자
        #print("qs는 " + qs)
        #instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html',{
        'post_list' : qs,
    })


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     # try:
#     #     post = Post.objects.get(pk=pk) # 앞 pk 필드 종류 뒤 pk 값을 넘긴거
#     # except Post.DoesNotExist:
#     #     raise Http404
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html',{
#         'post':post,

#     })

post_detail = DetailView.as_view(model=Post)