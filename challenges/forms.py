from django import forms
from .models import Challenge

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

class SubmissionForm(forms.Form):
    flag = forms.CharField(
        label="Introduce la Flag",
        widget=forms.TextInput(attrs={'placeholder': 'CTF{...}', 'class': 'form-control'})
    )
