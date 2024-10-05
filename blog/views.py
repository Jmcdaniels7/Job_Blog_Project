#Jacob McDaniels, 9/29/2024, 8:12pm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User, auth
from .forms import PostForm

def home(request):
    context = locals()
    template = 'blog/home.html'
    return render(request, template, context)

def homepage(request):
    context = locals()
    template = 'blog/home.html'
    return render(request, template, context)

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password==confirmpassword:
            if User.object.filter(email=email).exists():
                print('Email already in use')
            else:
                user = User.objects.create_user(firstname=firstname, lastname=lastname, email=email, password=password, confirmpassword=confirmpassword)
                user.save()
        else:
            print('Passwords do not match!')

    return render(request, 'blog/register.html')

def faq(request):
    context = locals()
    template = 'blog/faq.html'
    return render(request, template, context)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
#Jacob McDaniels, 10/5/2024, 10:44am