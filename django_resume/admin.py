from django_resume import models as resume_models
from django.contrib import admin
from django_resume.forms import WorkExperienceTaskInlineForm, WorkExperienceSkillInlineForm

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'degree', 'graduation', 'major', 'minor')
    
admin.site.register(resume_models.Education, EducationAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    
admin.site.register(resume_models.Skill, SkillAdmin)

class SkillInline(admin.TabularInline):
    model = resume_models.Skill
    form = WorkExperienceTaskInlineForm
    sortable_field_name = 'position'
    extra = 0 

class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [ SkillInline ]
    
admin.site.register(resume_models.SkillCategory, SkillCategoryAdmin)

class WorkExperienceTaskInline(admin.TabularInline):
    model = resume_models.WorkExperienceTask
    form = WorkExperienceTaskInlineForm
    sortable_field_name = 'position'
    extra = 0

class WorkExperienceSkillInline(admin.TabularInline):
    model = resume_models.WorkExperienceSkill
    form = WorkExperienceSkillInlineForm
    sortable_field_name = "position"
    extra = 0

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'dates', 'job_title', 'position',)
    list_editable = ('dates', 'job_title', 'position',)
    exclude = ('skills',)
    
    inlines = [
        WorkExperienceTaskInline,
        WorkExperienceSkillInline,
    ]
    
admin.site.register(resume_models.WorkExperience, WorkExperienceAdmin)

class OtherInfoAdmin(admin.ModelAdmin):
    fields = ('key', 'title', 'content')
    
admin.site.register(resume_models.OtherInfo, OtherInfoAdmin)