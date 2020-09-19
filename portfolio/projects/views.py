import json
from collections import Counter
from django.shortcuts import render, get_object_or_404
from users.models import User
from projects.models import Project, Education, Experience


def main(request, username):
    user = get_object_or_404(User, name=username)
    projects = Project.objects.all().filter(user=user)
    educations = Education.objects.all().filter(user=user)
    experience = Experience.objects.all().filter(user=user)

    skill_data = []
    project_names = []
    project_duration = []
    for project in projects:
        skill_data.extend(project.used_skills.all())
        project_names.append(project.name)
        project_duration.append(project.get_duration_days)
    skill_data = Counter(skill_data)
    labels = []
    counter_data = []
    for key, val in skill_data.items():
        labels.append(key.name)
        counter_data.append(str(val))

    skill_labels = ",".join(labels)
    skill_counter_data = ",".join(counter_data)
    project_duration = ",".join(project_duration)
    project_names = ",".join(project_names)

    data = {
        'user': user,
        'projects': projects,
        'educations': educations,
        'experience': experience,
        'skill_labels': skill_labels,
        'skill_counter_data': skill_counter_data,
        'project_duration': project_duration,
        'project_names': project_names
    }
    return render(request, 'index.html', data)
