from django.shortcuts import render
from users.models import User
from projects.models import Project, Education, Experience


def main(request, username):
    user = User.objects.get(name=username)
    projects = Project.objects.all().filter(user=user)
    educations = Education.objects.all().filter(user=user)
    experience = Experience.objects.all().filter(user=user)
    data = {
        'user': user,
        'projects': projects,
        'educations': educations,
        'experience': experience
    }
    return render(request, 'index.html', data)
