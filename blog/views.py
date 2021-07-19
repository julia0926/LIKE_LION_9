from django.http import request
from django.shortcuts import redirect, render,get_object_or_404 
from django.utils import timezone
from .forms import PostForm,CommentForm,HashtagForm
from .models import Blog,Hashtag
# Create your views here.

#메인페이지
def main(request):
    blogs = Blog.objects.all() #Blog 객체의 값들을 모두 가져옴
    hashtags = Hashtag.objects.all()
    return render(request, 'blog/main.html', {'blogs':blogs,'hashtags':hashtags})

# 글 작성 페이지 
def write(request):
    return render(request, 'blog/write.html')

#글 작성 함수
def create(request):
    if request.method == 'POST': #POST 메소드 방식인지 확인 
        form = PostForm(request.POST,request.FILES) #POST방식으로 요청받은 form을 변수에 저장
        if form.is_valid(): #유효한지 검사
            form=form.save(commit=False) 
            form.pub_date=timezone.now()
            form.save()
            return redirect('main') #form을 잘 입력했으면 main페이지로 이동 
    else: #유효하지 않으면 다시 검사해서 
        form=PostForm
        return render(request,'blog/write.html',{'form':form}) #다시 작성하게함

#수정페이지 (write페이지와 동일)
def edit(request,id): 
    post = get_object_or_404(Blog,id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) #수정해야 할 글의 id를 함수에게 전달
        if form.is_valid():
            form.save(commit=False)
            form.save()
            form.save_m2m()
            return redirect('detail',id)
    else:
        form=PostForm(instance=post)
        return render(request, 'blog/edit.html',{'form':form})

#삭제페이지
def delete(request, id):
    delete_blog=Blog.objects.get(id=id) #삭제할 글의 id를 가져와
    delete_blog.delete() # 삭제
    return redirect('main') #메인페이지로 이동 

#디테일 페이지 + 댓글
def detail(request, id):
    blog = get_object_or_404(Blog, id = id) 
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post_id=blog
            comment.text=form.cleaned_data['text']
            comment.save()
            return redirect('detail',id)
    else:
        form = CommentForm()
        return render(request, 'blog/detail.html', {'blog':blog,'form':form})

#해쉬태그 함수
def hashtagform(request,hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST,instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message= "이미 존재하는 해시태그 입니다."
                return render(request, 'blog/hashtag.html',{'form':form,'error_message':error_message})
            else:
                hashtag.name=form.cleaned_data['name']
                hashtag.save()
            return redirect('main')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'blog/hashtag.html',{'form':form})

def search(request, hashtag_id):
        hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
        return render(request, 'blog/search.html', {'hashtag':hashtag})