#Jacob McDaniels, 9/29/2024, 8:12pm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User, auth
from django.contrib import messages  # For user feedback
from .models import Post, Review
from .forms import PostForm

# this is a view to what page opens when the website is first visited
def home(request):
    template = 'blog/home.html'
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, template, {'posts': posts})

# This is for the home button on base.html to work
def homepage(request):
    template = 'blog/home.html'
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, template, {'posts': posts})

#login view
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login, username or password is not registered')
            return redirect('login')

    else:
        return render(request, 'blog/login.html')
    
#logout view
def logout(request):
    auth.logout(request)
    return redirect('/')



# User registration view
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(email=email).exists():  # checks for existing email
                messages.info(request, 'Email is already in use.') 
                return redirect('register') #redirects the page back to register.html with message
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already in use.')
                return redirect('register')
            else:
                #This saves a user in the database
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname, email=email, password=password, username=username
                )
                user.save()
                messages.info(request, 'Account created successfully.')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'blog/register.html')

# FAQ page view
def faq(request):
    template = 'blog/faq.html'
    return render(request, template)

# List of all posts (published)
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Post detail view
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create a new post
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

# Edit an existing post
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

# Add a new review to a post
def add_review(request):
    if request.method == "POST":
        rating = request.POST['rating']
        comment = request.POST['comment']
        createdDate = request.POST['created_date']
        publishedDate = request.POST['published_date']

        review = Review.objects.create_review(
            rating=rating, comment=comment, createdDate=createdDate, publishedDate=publishedDate
        )
        review.save()
        return redirect('/')

    return render(request, 'blog/add_review.html')

#Jacob McDaniels, 10/11/2024, 7:08pm

#Eric Valle 10/12/2024, 1:00am

# This is for the profile page on base.html to work
def profile(request):
    template = 'blog/profile.html'
    return render(request, template)

#Eric Valle 10/12/2024, 1:00am
