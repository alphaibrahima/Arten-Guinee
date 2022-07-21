from django import forms
from .models import Post
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget




class AnnonceForm(forms.ModelForm):
    class Meta:

        model = Post 
        fields = ('titre', 'tags', 'img_une', 'author', 'body')

        widgets = {
            'titre' : forms.TextInput(attrs={'class' : 'form-control', 'label':'Titre :', 'placeholder': 'Entrez votre titre...'}),
            'tags' : forms.TextInput(attrs={'class' : 'form-control',   'type' : 'text', 'data-role' : 'tagsinput' }),
            'author' : forms.TextInput(attrs={'class' : 'form-control', 'value' : '', 'id' : 'username', 'type' : 'hidden' }),
            # 'description' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Entrez Une Description ...'}),
            # 'description' : SummernoteWidget(),
            'body' : SummernoteWidget(),

        }


class UpdateForm(forms.ModelForm):
    class Meta:

        model = Post 
        fields = ('titre','tags', 'img_une', 'body')

        widgets = {
            'titre' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Entrez votre titre...'}),
            # 'description' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Entrez Une Description ...'}),
            # 'description' : SummernoteWidget(),
            'body' : SummernoteWidget(),
            
        }

        