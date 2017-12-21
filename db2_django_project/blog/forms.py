from django import forms
from blog.models import Comment

SORT_CHOICES = (
    ('country', 'Sort by country'),
    ('city', 'Sort by city'),
)


class SearchForm(forms.Form):
    """
    Create form for searching by word.
    """
    search_text = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control ml-sm-2 mr-sm-2',
        }), required=False)
    sort_by = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={
            'class': 'ml-sm-2 mr-sm-2',
        }), choices=SORT_CHOICES, required=False)


class CommentForm(forms.ModelForm):
    """
    Generates a form for adding comment to article.
    """
    class Meta:
        model = Comment
        fields = ['body']
