# Generated by Django 5.0 on 2024-01-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0006_academicemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectclass', models.CharField(max_length=260)),
                ('subjectstatus', models.IntegerField(default=1)),
            ],
        ),
    ]
