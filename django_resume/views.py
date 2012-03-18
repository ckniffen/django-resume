from django.shortcuts import render_to_response
from django_resume.models import WorkExperience, SkillCategory, OtherInfo, Education

from django.template.context import RequestContext# Create your views here.

def resume(request):
    skill_category_list = SkillCategory.objects.with_skills_in_skill_list()
    experience_list = WorkExperience.objects.all()
    education_list = Education.objects.all()
    
    # Retrieve Other info and put it into a dict with the OtherInfo.key being the key
    other_info = {}
    
    for info in OtherInfo.objects.all():
        other_info[info.key] = info
    
    context_data = {
        'other_info' : other_info,
        'skill_category_list' : skill_category_list,
        'experience_list' : experience_list,
        'education_list' : education_list,
    }
    
    return render_to_response('resume/resume.html', context_data, context_instance=RequestContext(request))