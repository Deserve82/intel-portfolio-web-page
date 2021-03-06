# Generated by Django 3.1.1 on 2020-09-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='graduate_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='type',
            field=models.CharField(choices=[('HS', 'HIGHSCHOOL'), ('COL', 'COLLEAGE'), ('UNIV', 'UNIVERSITY'), ('GS', 'GRADUATE_SCHOOL')], max_length=6),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(),
        ),
    ]
