from django.db import models
from users.models import User


class ProgrammingSkill(models.Model):
    name = models.CharField(max_length=25, blank=False, unique=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    school_type = (
        ('HS', 'HIGHSCHOOL'),
        ('COL', 'COLLEAGE'),
        ('UNIV', 'UNIVERSITY'),
        ('GS', 'GRADUATE_SCHOOL')
    )
    type = models.CharField(max_length=6, choices=school_type)
    name = models.CharField(max_length=20, blank=False)
    major = models.CharField(max_length=20, blank=True)
    start_date = models.DateField(blank=True)
    graduate_date = models.DateField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' 학력 사항'

    @property
    def get_duration_days(self):
        return (self.graduate_date - self.start_date).days


class Experience(models.Model):
    level = (
        ('IN', 'INTERN'),
        ('JU', 'JUNIOR'),
        ('SE', 'SENIOR'),
        ('MA', 'MANAGER')
    )
    role = models.CharField(max_length=5, choices=level)
    company_name = models.CharField(max_length=30, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' 경력 사항'


class Project(models.Model):
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=255, blank=False)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    used_skills = models.ManyToManyField(ProgrammingSkill)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' 프로젝트'

    @property
    def get_duration_days(self):
        return str(abs((self.end_date - self.start_date).days))
