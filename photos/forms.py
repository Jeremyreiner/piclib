from django import forms 
from .models import PhotoImage

PhotoImageFormSet = forms.modelformset_factory(PhotoImage, fields=['image'])