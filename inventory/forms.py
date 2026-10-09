from django import forms
from .models import DeviceRepair

class RepairForm(forms.ModelForm):
    class Meta:
        model = DeviceRepair
        fields = ['model_name', 'features', 'problem', 'phone_number']
        widgets = {
            'model_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Наприклад: Pixel 7, iPhone 13 або Redmi Note 12 5G'
            }),
            'features': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Стан екрану, об\'єм пам\'яті тощо'
            }),
            'problem': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 4,
                'placeholder': 'Опишіть, що саме не працює'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+380...'
            }),
        }