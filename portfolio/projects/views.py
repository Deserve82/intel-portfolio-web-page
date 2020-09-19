import json
from collections import Counter
from django.shortcuts import render
from users.models import User
from projects.models import Project, Education, Experience


def main(request, username):
    user = User.objects.get(name=username)
    projects = Project.objects.all().filter(user=user)
    educations = Education.objects.all().filter(user=user)
    experience = Experience.objects.all().filter(user=user)

    skill_data = []
    for project in projects:
        skill_data.extend(project.used_skills.all())
    skill_data = Counter(skill_data)
    labels = []
    counter_data = []
    for key, val in skill_data.items():
        labels.append(key.name)
        counter_data.append(str(val))

    labels = ",".join(labels)
    counter_data = ",".join(counter_data)

    data = {
        'user': user,
        'projects': projects,
        'educations': educations,
        'experience': experience,
        'labels': labels,
        'counter_data': counter_data
    }
    return render(request, 'index.html', data)
