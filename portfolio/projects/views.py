import json
from collections import Counter
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from users.models import User
from projects.models import Project, Education, Experience


def home(request):
    return render(request, 'home.html')


def main(request, username):
    if request.method == 'GET':
        # I could use user_id instead of username, but I thought the username was more clear to read.
        user = get_object_or_404(User, name=username)
        projects = Project.objects.all().filter(user=user)
        educations = Education.objects.all().filter(user=user)
        experiences = Experience.objects.all().filter(user=user)

        # get project's used skills for chart.js.
        skill_data = []  # ['Python', 'Python', 'Python', 'Flask', 'Flask','Java']
        project_names = []  # ['project1', 'project2']
        project_duration = []  # ['30', '70']
        for project in projects:
            skill_data.extend(project.used_skills.all())
            project_names.append(project.name)
            project_duration.append(project.get_duration_days)

        # for easy parsing in js, split Countered data into two arrays.
        skill_data = Counter(skill_data)
        labels = []  # ['Python', 'Flask', 'Java']
        counter_data = []  # ['3', '2', '1']
        for key, val in skill_data.items():
            labels.append(key.name)
            counter_data.append(str(val))

        # decided to use only django and vanilla js, So had to parse with string type.
        skill_labels = ",".join(labels)
        skill_counter_data = ",".join(counter_data)
        project_duration = ",".join(project_duration)
        project_names = ",".join(project_names)

        data = {
            'user': user,
            'projects': projects,
            'educations': educations,
            'experiences': experiences,
            'skill_labels': skill_labels,
            'skill_counter_data': skill_counter_data,
            'project_duration': project_duration,
            'project_names': project_names
        }
        return render(request, 'index.html', data)
    else:
        return HttpResponse('this method is not allowed')
