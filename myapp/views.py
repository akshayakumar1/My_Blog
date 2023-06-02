from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib  import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import *
from .forms import Contact_form
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def main(request):
    # return HttpResponse('<h1>welcome to home page!..</h1>') 
    return render(request,'main.html')


def home(request):

    return render(request,'home.html')



# registering  user
def regeister(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        uname = request.POST.get('uname')
        # print(fname, lname, email, passwd, uname)
        if User.objects.filter(email=email).exists():
            messages.warning(request,'email allready exist!.')
            return redirect('regeister')
        else:
            user = User(first_name=fname,last_name=lname,email=email, password=passwd,username=uname)
            user.set_password(passwd)
            user.save()
            subject ="about your registrations"
            message = f"Hii {uname} you have been register susccessfully on my Bolg"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail(subject, message, from_email, recipient_list,fail_silently=False,)

            # send_mail("about your registrations",f"Hii {uname} you have been register susccessfully on my Bolg","kakshaya844@gmail.com",[email,],fail_silently=False,)

            messages.success(request, 'user registerded succesfully')
            return redirect('login')

    
    return render(request,'regeister.html')



#creating login user
def user_login(request):
    if request.method == "POST":
        user_name = request.POST["uname"]
        passwd = request.POST["passwd"]
        user = authenticate(request, username=user_name, password=passwd)
        if user is not None:
            login(request,user)
            # Redirect to a success page
            messages.success(request,'login success')
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.warning(request,'invalid login')
            return redirect('login')
        
    return render(request,'login.html')


# user log-out
def user_logout(request):
    logout(request)
    messages.success(request,'user logout succecfully!')
    return redirect('login')



#user  createing blog post
def blog_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        img = request.FILES['image']
        # print(">>>>>>>>>>>>>>>>>")
        # print(title)
        # print(content)
        if title and content and img:
            blog = Blog(title=title,content=content,Img=img,uid=request.user)
            blog.save()
            messages.success(request,'post cratetaedd succecfully...')
            return redirect('all_posts')
        else:
            messages.warning(request,'filds should be fills..')
            return redirect('blog_post')
    return render(request,'blog_post.html')

#displaying all posts
def display_all_post(request):
    # all_posts = Blog.objects.all()
    all_posts = Blog.objects.filter(uid=request.user) # only resgister user can see theri post not othsers..)
    print(">>>>>>>>>>>>>")
    print(all_posts)
    return render(request,'all_posts.html',{'posts':all_posts})

# displaying perticular post
def display_post(request,id):
    post = Blog.objects.get(id=id)
    print(post)
    return render(request,'post_details.html',{'post':post})

#editing post
def edit_post (request,id):
    edit_blog =Blog.objects.get(id=id)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_content = request.POST.get('content')
        edit_blog.title = new_title
        edit_blog.content =new_content
        edit_blog.save()

        messages.success(request,"post edited successfully")
        return redirect('all_posts')
    return render(request,'edit_post.html',{"post":edit_blog})


#deleting particular one post 
def delete_post(request,id):
    delete_post = Blog.objects.get(id = id)
    delete_post.delete()
    messages.warning(request,"post deleted successfully")
    return redirect('all_posts')


# user contacting  us
def contact(request):
    # form = Contact()
    form =Contact_form()

    if request.method == "POST":
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'thank you for your feedback!.')
            # return redirect('home')
            return redirect('home')  
    return render(request,'contact_us.html',{"form":form})
'''
#user changing password
def change_password(request):
    if request.method == "POST":
        new_pass = request.POST.get('new_passwd')
        reqUser = User.objects.get(username=request.user.username)
        reqUser.set_password(new_pass)
        reqUser.save()
        messages.success(request,'password change successfully.!')
        return redirect("home")
    return render(request,'change_pass.html')
'''
#user changing password using builtin method
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user =form.save()
            update_session_auth_hash(request, user)  #if we not use this function then after change thr password user =atoumaticaly logout
            messages.success(request,'password change successfully.!')
            return redirect("home")
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect("change_password")
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'change_pass.html',{"form":form})

#change username
def change_username(request):
    if request.method == "POST":
        new_username = request.POST.get('new_username')
        reqUser = User.objects.get(username=request.user.username)
        reqUser.username =new_username
        reqUser.save()
        messages.success(request,'user name change successfully.!')
        return redirect("home")
    return render(request,'change_username.html')