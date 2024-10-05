#Jacob McDaniels, 9/29/2024, 8:12pm
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/home', views.homepage, name='home'),
    path('blog/post_list', views.post_list, name='post_list'),
    path('blog/register/', views.register, name='register'),
    path('blog/faq', views.faq, name='faq'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
#Jacob McDaniels, 9/29/2024, 9:30pm