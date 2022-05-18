# Generated by Django 4.0.4 on 2022-05-18 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.TextField()),
                ('correct_solution', models.FileField(upload_to='documents/')),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tutorial')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_solution', models.FileField(upload_to='')),
                ('status', models.CharField(choices=[('Uploaded', 'Uploaded'), ('Review', 'Review'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], default='Uploaded', max_length=255)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolutionComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.exercisesolution')),
            ],
        ),
    ]