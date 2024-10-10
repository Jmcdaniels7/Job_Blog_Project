#Jacob McDaniels, 9/29/2024, 8:12pm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages  # For user feedback
from .models import Post, Review
from .forms import PostForm, ReviewForm

# Home page view
def home(request):
    template = 'blog/home.html'
    return render(request, template)

# Another homepage (possibly redundant, consider merging)
def homepage(request):
    template = 'blog/home.html'
    return render(request, template)

# User registration view
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(email=email).exists():  # Fixed typo
                messages.error(request, 'Email is already in use.')
            else:
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname, email=email, password=password
                )
                user.save()
                messages.success(request, 'Account created successfully.')
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match.')

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

# List all reviews for a post
def review_list(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    reviews = post.reviews.all()  # Access all reviews for this post
    return render(request, 'reviews/review_list.html', {'post': post, 'reviews': reviews})

# View details of a specific review
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

# Add a new review to a post
def add_review(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.post = post
            review.created_date = timezone.now()
            review.save()
            return redirect('review_list', post_id=post.pk)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})

#Jacob McDaniels, 10/5/2024, 10:44am
#Kendal Jackson, 10/10/24, 10:29am