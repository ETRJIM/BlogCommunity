from django import forms
from blog.models import BlogPost,BlogComment
from django.contrib.auth.forms import UserCreationForm

class BlogPostForm(forms.ModelForm):

    class Meta():
        model = BlogPost
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class BlogCommentForm(forms.ModelForm):

    class Meta():
        model = BlogComment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }

