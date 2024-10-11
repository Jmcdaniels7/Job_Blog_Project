#Jacob McDaniels, 9/29/2024, 8:12pm
from django.urls import path
from . import views

urlpatterns = [
    # Home and blog-related paths
    path('', views.home, name='home'),
    path('blog/home/', views.homepage, name='homepage'),
    path('blog/post_list/', views.post_list, name='post_list'),
    path('blog/register', views.register, name='register'),
    path('blog/faq/', views.faq, name='faq'),

    # Post-related paths
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # Review-related paths
    # Our feedback button should lead us to a page where a user can make a review on our page
    # Then that data will get sent to the data base.
    path('post/<int:pk>/reviews/', views.review_list, name='review_list'),  # Changed post_id to pk
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    path('post/<int:pk>/reviews/add/', views.add_review, name='add_review'),  # Changed post_id to pk
]


#Jacob McDaniels, 9/29/2024, 9:30pm
#Kendal Jackson, 10/10/24, 10:30am
#Jacob McDaniels, 10/11/2024, 1:49pm