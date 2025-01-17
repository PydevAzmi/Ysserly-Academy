# Generated by Django 4.2 on 2024-07-17 18:25

import courses.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('university', models.CharField(choices=[('Mansoura', 'Mansoura'), ('Tanta', 'Tanta'), ('Ain Shams', 'Ain Shams'), ('Cairo', 'Cairo'), ('Other', 'Other')], max_length=50, verbose_name='University')),
                ('specialist', models.CharField(blank=True, max_length=50, null=True, verbose_name='Specialist')),
                ('college', models.CharField(choices=[('Medicine', 'Medicine'), ('Science', 'Science'), ('Technology', 'Technology'), ('Engineering', 'Engineering'), ('Other', 'Other')], max_length=50, verbose_name='College')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='courses.course', verbose_name='Course')),
            ],
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(verbose_name='Video Link')),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Upload Date')),
                ('lecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='courses.lecture', verbose_name='lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('university', models.CharField(choices=[('Mansoura', 'Mansoura'), ('Tanta', 'Tanta'), ('Ain Shams', 'Ain Shams'), ('Cairo', 'Cairo'), ('Other', 'Other')], max_length=50, verbose_name='University')),
                ('specialist', models.CharField(blank=True, max_length=50, null=True, verbose_name='Specialist')),
                ('college', models.CharField(choices=[('Medicine', 'Medicine'), ('Science', 'Science'), ('Technology', 'Technology'), ('Engineering', 'Engineering'), ('Other', 'Other')], max_length=50, verbose_name='College')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Year')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=50, verbose_name='Status')),
                ('request_date', models.DateTimeField(auto_now_add=True, verbose_name='Request Date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='courses.course', verbose_name='Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='courses.student', verbose_name='Student')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('university', models.CharField(choices=[('Mansoura', 'Mansoura'), ('Tanta', 'Tanta'), ('Ain Shams', 'Ain Shams'), ('Cairo', 'Cairo'), ('Other', 'Other')], max_length=50, verbose_name='University')),
                ('specialist', models.CharField(blank=True, max_length=50, null=True, verbose_name='Specialist')),
                ('college', models.CharField(choices=[('Medicine', 'Medicine'), ('Science', 'Science'), ('Technology', 'Technology'), ('Engineering', 'Engineering'), ('Other', 'Other')], max_length=50, verbose_name='College')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bio', models.CharField(blank=True, max_length=150, null=True, verbose_name='Bio')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='professor_profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('read', models.BooleanField(default=False, verbose_name='Read')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=courses.models.file_path, verbose_name='File')),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Upload Date')),
                ('lecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='courses.lecture', verbose_name='lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enrollment_date', models.DateTimeField(auto_now_add=True, verbose_name='Enrollment Date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='courses.course', verbose_name='Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='courses.student', verbose_name='Student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.professor', verbose_name='professor'),
        ),
    ]
