# Generated by Django 4.0.4 on 2022-05-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_exercise_exercisesolution_solutioncomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutioncomment',
            name='fixed_solution',
            field=models.FileField(null=True, upload_to='fixed_solution/'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='correct_solution',
            field=models.FileField(upload_to='correct_solution/'),
        ),
        migrations.AlterField(
            model_name='exercisesolution',
            name='user_solution',
            field=models.FileField(upload_to='user_solution/'),
        ),
    ]