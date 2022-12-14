# Generated by Django 4.1 on 2022-09-02 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='classes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='account.classes'),
        ),
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.ManyToManyField(related_name='subject_student', to='account.subject'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='classes',
            field=models.ManyToManyField(related_name='teacher_class', to='account.classes'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='subject_teacher', to='account.subject'),
        ),
    ]
