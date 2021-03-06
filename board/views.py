from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import User,Idea,Comment,Message
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.hashers import check_password
import json
from .forms import IdeaForm
from django_email_verification import sendConfirm
from django.template.loader import render_to_string


def index(request):
    return render(request,'board/index.html')

def about_site(request):
    return render(request,'board/about_site.html')

@login_required
def idea_list(request):
    form=Idea.objects.all()
    user=request.user
    return render(request,'board/idea_list.html',{'form':form,'user':user})

@login_required
def likes_process(request):
    idea=Idea.objects.get(pk=request.POST['pk'])
    user=request.user

    if idea.likes.filter(id=user.id).exists():
        idea.likes.remove(user)
        idea.author.thinker_likes-=1
        idea.author.save()
        flag=False
    else:
        idea.likes.add(user)
        idea.author.thinker_likes+=1
        idea.author.save()
        flag=True

    message=idea.likes.count()
    context={'message':str(message)+'명','flag':flag}
    return HttpResponse(json.dumps(context),content_type='application/json')


@login_required
def idea_delete(request,pk):
    idea=Idea.objects.get(pk=pk)
    idea.delete()
    return redirect('board:idea_list')

@login_required
def idea_new(request):
    if request.method=="POST":
        form=IdeaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board:idea_list')
    else:
        form = IdeaForm()
    return render(request,'board/idea_edit.html',{'form':form})

@login_required
def idea_edit(request,pk):
    post = get_object_or_404(Idea, pk=pk)
    user=request.user
    if post.author==user:
        if request.method == "POST":
            form = IdeaForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('board:idea_list')
        else:
            user=request.user
            form = IdeaForm(instance=post)
        return render(request,'board/idea_edit.html',{'form':form,'post':post})
    else:
       return render(request,'board/idea_detail.html',{'post':post}) 

def signin(request):
    return render(request,'board/signin.html')

def signin_fail(request):
    return render(request,'board/signin_fail.html')

def signin_success(request):
    return render(request,'board/signin_success.html',{'username':request.user.username})

def signin_need(request):
    return render(request,'board/signin_need.html')

def signin_process(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        user=request.user
        user.update_thinker_status()
        if request.POST.get('remember'):
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE=False
        else:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE=True
        
        return HttpResponseRedirect(reverse('board:signin_success'))
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect(reverse('board:signin_fail'))






def signup(request):
    return render(request,'board/signup.html')

def signup_fail(request,error):
    return render(request,'board/signup_fail.html',{'error':error})

def signup_success(request):
    return render(request,'board/signup_success.html')

def signup_process(request):
    try: 
        User.objects.get(username=request.POST['username'])
        return HttpResponseRedirect(reverse('board:signup_fail',args=('username',)))  
    except:
        username=request.POST['username']

    if request.POST['password']!=request.POST['confirm']:
        return HttpResponseRedirect(reverse('board:signup_fail',args=('password',))) 
    password= request.POST['password']
    email=request.POST['email']
    # Add session!!
    user=User.objects.create_user(username=username,password=password,email=email)
    sendConfirm(user)
    return HttpResponseRedirect(reverse('board:signup_success')) 

def logout_process(request):
    logout(request)
    return HttpResponseRedirect(reverse('board:logout_success'))

def logout_success(request):
    return render(request,'board/index.html')

def user_update(request):
    return render(request,'board/user_update.html')

def user_update_process(request):
    if check_password(request.POST['origin_password'],request.user.password):
        if request.POST['password']=='':
            user=User.objects.get(username=request.user.username)
            user.email=request.POST['email']
            user.save()
            return HttpResponseRedirect(reverse('board:user_update_success'))
        else:
            if request.POST['password']!=request.POST['confirm']:
                return HttpResponseRedirect(reverse('board:user_update_fail',args=('새 비밀번호',))) 
            else:
                user=User.objects.get(username=request.user.username)
                user.email=request.POST['email']
                user.set_password(request.POST['password'])
                user.save()
                login(request,user)
                return HttpResponseRedirect(reverse('board:user_update_success')) 
    else:
        return HttpResponseRedirect(reverse('board:user_update_fail',args=('기존 비밀번호',))) 

def user_update_success(request):
    return render(request,'board/user_update_success.html')

def user_update_fail(request,error):
    return render(request,'board/user_update_fail.html',{'error':error})

def username_check(request):
   
    try:
        User.objects.get(username=request.POST['pk'])
        message='동일한 아이디가 존재합니다.'
    except:
        if request.POST['pk']=='':
            message='아이디를 입력해주세요.'
        else:
            message='가능한 아이디입니다!'
    
    context={'message':message}
    return HttpResponse(json.dumps(context),content_type='application/json')

def about_user(request):
    user=request.user
    return render(request,'board/about_user.html',{'user':user})

def user_idea(request):
    user=request.user
    return render(request,'board/user_idea.html',{'user':user})

def user_likes(request):
    user=request.user
    return render(request,'board/user_likes.html',{'user':user})

def application(request):
    return render(request,'board/application.html')

def feedback(request):
    return render(request,'board/feedback.html')

def motivation(request):
    return render(request,'board/motivation.html')

def add_comment(request):
    idea=Idea.objects.get(pk=request.POST['pk'])
    user=request.user
    comment=Comment.objects.create(for_idea=idea,author=user,article=request.POST['content'])
    html = render_to_string('board/comment_list.html',{'comment':comment,'user':user})

    context={'html':html,'article':comment.article,'author':comment.author.username}
    return HttpResponse(json.dumps(context),content_type='application/json')

def delete_comment(request):
    comment=Comment.objects.get(pk=request.POST['pk'])
    comment.delete()

    context={}
    return HttpResponse(json.dumps(context),content_type='application/json')

def update_comment(request):
    comment=Comment.objects.get(pk=request.POST['pk'])
    comment.article=request.POST['content']
    comment.save()

    context={'article':comment.article}
    return HttpResponse(json.dumps(context),content_type='application/json')