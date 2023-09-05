from django import forms
from .models import Route, Tag

class RouteAdminForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Route
        fields = '__all__'
        
        
