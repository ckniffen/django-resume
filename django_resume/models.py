from django.db import models

class Education(models.Model):
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=150)
    graduation = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    minor = models.CharField(max_length=100)
    involvement = models.TextField(default="", blank=True)
    
    def __unicode__(self):
        return self.school_name + ': ' + self.degree
    
    class Meta:
        verbose_name_plural = 'education'
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('SkillCategory', related_name='skills')
    overall_weight = models.DecimalField(decimal_places=2, max_digits=4, default = 0)
    position = models.IntegerField(default=0)
    show_in_skill_list = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('position',)

class SkillCategoryManager(models.Manager):
    def with_skills_in_skill_list(self):
        categories_with_skills_in_skill_list = []
        all_skill_categories = list(self.get_query_set())
        
        for category in all_skill_categories:
            if category.skills_in_skill_list.count() > 0:
                categories_with_skills_in_skill_list.append(category)
                
        return categories_with_skills_in_skill_list
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    
    objects = SkillCategoryManager()
    @property
    def skills_in_skill_list(self):
        return self.skills.filter(show_in_skill_list=True)
        
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'skill categories'

class WorkExperience(models.Model):
    company = models.CharField(max_length=200)
    dates = models.CharField(max_length=45)
    job_title = models.CharField(max_length=100)
    
    position = models.IntegerField(default=0)
    
    skills = models.ManyToManyField('Skill', through='WorkExperienceSkill')
    
    @property
    def skills_ordered(self):
        return self.skills.order_by('workexperienceskill__position')
    
    def __unicode__(self):
        return self.company + ": " + self.job_title
    
    class Meta:
        ordering = ('position',)
        
class WorkExperienceSkill(models.Model):
    work_experience = models.ForeignKey('WorkExperience')
    skill = models.ForeignKey('Skill')
    position = models.PositiveSmallIntegerField(blank=True, default=0)
        
    def __unicode__(self):
        return self.skill.name
    
    class Meta:
        ordering = ['position']

class WorkExperienceTask(models.Model):
    text = models.CharField(max_length=400)
    work_experience = models.ForeignKey('WorkExperience', related_name="tasks")
    position = models.PositiveSmallIntegerField(blank=True, default=0)
    
    def __unicode__(self):
        return self.text
    
    class Meta:
        ordering = ['position']
    
class OtherInfo(models.Model):
    key = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = 'other info section'