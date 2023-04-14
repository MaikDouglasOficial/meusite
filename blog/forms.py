from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)
        widgets = {
            'text': CKEditorWidget(attrs={'filebrowserUploadUrl': '/upload_image/'})
        }