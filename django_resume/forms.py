from django import forms
from django_resume.models import Skill, WorkExperienceSkill, WorkExperienceTask

class SkillInlineForm(forms.ModelForm):
    class Meta():
        model = Skill
        fields = ('name', 'position',)
        widgets = { 'position': forms.HiddenInput() }
        
class WorkExperienceTaskInlineForm(forms.ModelForm):
    class Meta():
        model = WorkExperienceTask
        widgets = {
            'text': forms.TextInput(attrs={ 'style': 'width: 700px' }),
            'position': forms.HiddenInput(),
        }
        
class WorkExperienceSkillInlineForm(forms.ModelForm):
    class Meta():
        model = WorkExperienceSkill
        widgets = { 'position': forms.HiddenInput() }