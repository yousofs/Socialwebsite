from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
