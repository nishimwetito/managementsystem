from django import forms
from .models import Member,GalleryImage,News,Sermon

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'  # Use this if you want all model fields


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'image']  # Adjust according to your model fields
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image title'
            }),
        }
        labels = {
            'title': 'Image Title',
            'image': 'Select Image',
        }




class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'summary', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter news title'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter a short summary'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter the full news content'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermon
        fields = ['title', 'preacher', 'thumbnail', 'document', 'video_url']