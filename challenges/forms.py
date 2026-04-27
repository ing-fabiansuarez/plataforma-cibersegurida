from django import forms
from .models import Challenge, Badge
import json

class ChallengeForm(forms.ModelForm):
    flag_raw = forms.CharField(
        label="Flag (Texto Plano)",
        widget=forms.TextInput(attrs={'placeholder': 'CTF{mi_flag_secreta}'}),
        help_text="La flag será hasheada automáticamente antes de guardarse."
    )

    class Meta:
        model = Challenge
        fields = [
            'title', 'description', 'category', 'difficulty', 
            'flag_case_sensitive', 'flag_regex', 'points', 
            'dynamic_scoring', 'external_resource_url', 'is_published'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class BadgeForm(forms.ModelForm):
    conditions_json = forms.CharField(
        label="Lógica de Desbloqueo",
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = Badge
        fields = [
            'name', 'description', 'category', 'subcategory', 
            'level', 'rarity', 'icon_url', 'is_secret', 'points_awarded',
            'prerequisites'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Hacker Novato'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe qué logros otorga esta insignia...'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Web, Forensics...'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'rarity': forms.Select(attrs={'class': 'form-select'}),
            'icon_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://ejemplo.com/icono.png'}),
            'points_awarded': forms.NumberInput(attrs={'class': 'form-control'}),
            'prerequisites': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.conditions:
            self.fields['conditions_json'].initial = json.dumps(self.instance.conditions)
        else:
            self.fields['conditions_json'].initial = '{}'

    def clean_conditions_json(self):
        data = self.cleaned_data['conditions_json']
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            raise forms.ValidationError("El formato JSON no es válido.")

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.conditions = self.cleaned_data['conditions_json']
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class SubmissionForm(forms.Form):
    flag = forms.CharField(
        label="Introduce la Flag",
        widget=forms.TextInput(attrs={'placeholder': 'CTF{...}', 'class': 'form-control'})
    )
