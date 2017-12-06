from django import forms

from petlist.models import Pets
from comment.models import CommentStruct


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentStruct
        fields=["comment_id","commentwords"]
