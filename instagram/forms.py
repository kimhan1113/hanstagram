from django.forms import ModelForm, Textarea

from instagram.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["photo", "caption", "location"]

        widgets = {
            "caption": Textarea,
        }