#from email import message
from django.shortcuts import render
from .models import Post
# Create your views here.
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