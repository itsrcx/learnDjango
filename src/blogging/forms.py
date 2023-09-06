from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')

    
class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','content','status')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Title size must not exceed 150 characters.'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'})
        }