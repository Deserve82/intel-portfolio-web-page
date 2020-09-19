from datetime import date, timedelta

from django.test import TestCase
from .models import Project, ProgrammingSkill, Education, Experience
from users.models import User


class ModelTestCase(TestCase):
    def setUp(self):
        self.start_date = date.today() - timedelta(days=30)
        self.end_date = date.today()

        self.user_name = "test_user"
        self.profile_image = "image_str"
        self.user = User(name=self.user_name, profile_image=self.profile_image)

        self.programming_name = "TEST"
        self.programming_skill = ProgrammingSkill(name=self.programming_name)

        self.school_name = "test_name"
        self.school_type = "HS"
        self.school = Education(name=self.school_name, type=self.school_type, user=self.user,
                                start_date=self.start_date, graduate_date=self.end_date)
        self.company_name = "intel"
        self.experience = Experience(user=self.user, company_name=self.company_name,
                                     start_date=self.start_date, end_date=self.end_date)

        self.project = Project(image=self.profile_image, user=self.user, start_date=self.start_date,
                               end_date=self.end_date)

    def test_model_count(self):
        old_count_user = User.objects.count()
        self.user.save()
        new_count_user = User.objects.count()
        self.assertNotEqual(old_count_user, new_count_user)

        old_count_skill = ProgrammingSkill.objects.count()
        self.programming_skill.save()
        new_count_skill = ProgrammingSkill.objects.count()
        self.assertNotEqual(old_count_skill, new_count_skill)

        old_count_edu = Education.objects.count()
        self.school.save()
        new_count_edu = Education.objects.count()
        self.assertNotEqual(old_count_edu, new_count_edu)

        old_count_exp = Experience.objects.count()
        self.experience.save()
        new_count_exp = Experience.objects.count()
        self.assertNotEqual(old_count_exp, new_count_exp)

        old_count_pro = Project.objects.count()
        self.project.save()
        new_count_pro = Project.objects.count()
        self.assertNotEqual(old_count_pro, new_count_pro)

    def test_many_to_many_field(self):
        self.user.save()
        self.programming_skill.save()
        self.project.save()
        self.project.used_skills.add(self.programming_skill)
        self.assertEqual(
            ProgrammingSkill.objects.count(),
            self.project.used_skills.count()
        )

    def test_get_duration_days(self):
        self.user.save()
        self.project.save()
        self.assertEqual(self.project.get_duration_days, '30')

