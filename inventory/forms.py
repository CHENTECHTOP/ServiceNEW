from django import forms
from .models import DeviceRepair, Review

class RepairForm(forms.ModelForm):
    class Meta:
        model = DeviceRepair
        fields = ['model_name', 'features', 'problem', 'phone_number']
        widgets = {
            'model_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Pixel 7, iPhone 13, Redmi Note 12...'}),
            'features': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Стан екрану, об\'єм пам\'яті тощо'}),
            'problem': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Опишіть проблему'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+380...'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author_name', 'rating', 'text']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваше ім\'я'}),
            'rating': forms.Select(choices=[(i, f"{i} ★") for i in range(5, 0, -1)], attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Ваш відгук про ремонт...'}),
        }