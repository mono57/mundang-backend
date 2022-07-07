from django import forms

from blog.models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'type', 'summary', 'content', 'category', 'cover_image', 'published')
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 2})
        }

