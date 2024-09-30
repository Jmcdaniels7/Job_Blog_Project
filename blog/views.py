#Jacob McDaniels, 9/29/2024, 8:12pm
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def home(request):
    context = locals()
    template = 'blog/home.html'
    return render(request, template, context)

def homepage(request):
    context = locals()
    template = 'blog/home.html'
    return render(request, template, context)

def register(request):
    context = locals()
    template = 'blog/register.html'
    return render(request, template, context)

def faq(request):
    context = locals()
    template = 'blog/faq.html'
    return render(request, template, context)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
#Jacob McDaniels, 9/30/2024, 3:39pm