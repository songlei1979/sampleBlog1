from django.forms import ModelForm, TextInput, Select, Textarea, SelectDateWidget

from blog.models import Post, Category, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tab', 'snippet', 'author', 'body', 'category', 'header_image')
        widgets = {
            'title': TextInput(attrs={'class':'form-control', 'placeholder':'Type your title here'}),
            'title_tab': TextInput(attrs={'class': 'form-control'}),
            'snippet': TextInput(attrs={'class': 'form-control'}),
            # 'author': Select(attrs={'class': 'form-control'}),
            'author': TextInput(attrs={'class': 'form-control', 'value':'', 'id':'userinput', 'type':'hidden'}),
            'body': Textarea(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'})
            # 'category': Select(choices=categoryChoices, attrs={'class': 'form-control'}),
        }

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control'}),
            }