#Jacob McDaniels, 9/29/2024, 8:12pm
from django.urls import path
from . import views

urlpatterns = [
    # Home and blog-related paths
    path('', views.home, name='home'),
    path('blog/home/', views.homepage, name='homepage'),
    path('blog/post_list/', views.post_list, name='post_list'),
    path('blog/register/', views.register, name='register'),
    path('blog/faq/', views.faq, name='faq'),

    # Post-related paths
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # Review-related paths
    # Our feedback button should lead us to a page where a user can make a review on our page
    # Then that data will get sent to the data base.
    path('blog/add_review/', views.add_review, name='add_review'), 

    #login and logout path
    path('blog/login/', views.login, name='login'),
    path('blog/logout/', views.logout, name='logout'),
]
#Jacob McDaniels, 10/11/2024, 7:07pm