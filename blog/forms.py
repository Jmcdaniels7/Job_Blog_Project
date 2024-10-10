from django import forms
from .models import Post, Review

# Form for creating or editing a Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title here'}),
            'text': forms.Textarea(attrs={'placeholder': 'Write your post here'}),
        }
        labels = {
            'title': 'Post Title',
            'text': 'Post Content',
        }

# Form for adding a new Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
    
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating

#Kendal Jackson, 10/10/24, 10:34am