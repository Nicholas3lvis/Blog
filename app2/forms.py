from django import forms
from . models import Blog, Category, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','category','body','img']
        
        
        
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter The Title'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-select', 'placeholder':'Enter Your UserName'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Your Adress'}))
    img = forms.ImageField(widget=forms.FileInput())


class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Share your Comment about the content'}))

    