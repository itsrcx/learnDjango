from .models import Comment, Post, Category
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')

choices = Category.objects.all().values_list('name','name')

choice_list = []
for item in choices:
    choice_list.append(item)

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','slug','author','category','content','status')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Title size must not exceed 150 characters.'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'})
        }