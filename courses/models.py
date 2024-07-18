from django.db import models
from django.db.models import Q
import uuid
from project.settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _

UNIVERSITY_CHOICES = [
    ('Mansoura',_('Mansoura')),
    ('Tanta',_('Tanta')),
    ('Ain Shams',_('Ain Shams')),
    ('Cairo',_('Cairo')),
    ('Other',_('Other')),
]

COLLEGE_CHOICES = [
    ("Medicine", _("Medicine")),
    ("Science", _("Science")),
    ("Technology", _("Technology")),
    ("Engineering", _("Engineering")),
    ('Other',_('Other')),
]

STATUS_CHOICES = [
    ('Pending', _('Pending')),
    ('Approved', _('Approved')),
    ('Declined', _('Declined')),
]

def file_path(instance, file_name):
    return f"files/{instance.lecture.course.professor}/{instance.lecture.course.title}/{instance.lecture.title}/{file_name}"

def file_path_image(instance, file_name):
    return f"files/{instance.professor}/courses/{instance.title}/{file_name}"

class EducationScope(models.Model):
    university = models.CharField(_("University"), max_length=50, choices=UNIVERSITY_CHOICES)
    specialist = models.CharField(_("Specialist"), max_length=50, null=True, blank=True)
    college = models.CharField(_("College"), max_length=50, choices=COLLEGE_CHOICES)

    class Meta:
        abstract=True  

class Professor(EducationScope):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(AUTH_USER_MODEL, verbose_name=_("User"), related_name="professor_profile", on_delete=models.CASCADE)
    bio = models.CharField(_("Bio"), max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return f'Prof. {self.user.username}'

class Student(EducationScope):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(AUTH_USER_MODEL, verbose_name=_("User"), related_name="student_profile", on_delete=models.CASCADE)
    year = models.PositiveIntegerField(verbose_name=_("Year"), null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user.username}'

class Course(EducationScope):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"))
    image = models.FileField(_("Course Image"), upload_to=file_path_image, max_length=100, null=True, blank=True)
    professor = models.ForeignKey(Professor, verbose_name=_("professor"), related_name="courses", on_delete=models.CASCADE)
    date = models.DateField(verbose_name=_("Date"), null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title}'

class Lecture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(_("Title"),max_length=255)
    upload_date = models.DateTimeField(_("Upload Date"),auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.title} - {self.course}'

class FileContent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(_("File"), upload_to=file_path, max_length=100)
    lecture = models.ForeignKey(Lecture, verbose_name=_("lecture"), related_name="files", on_delete=models.CASCADE, null=True, blank=True)
    upload_date = models.DateTimeField(_("Upload Date"),auto_now_add=True, null=True, blank=True)

class VideoContent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(_("Video Link"), max_length=200)
    lecture = models.ForeignKey(Lecture, verbose_name=_("lecture"), related_name="videos", on_delete=models.CASCADE, null=True, blank=True)
    upload_date = models.DateTimeField(_("Upload Date"),auto_now_add=True, null=True, blank=True)

class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student,verbose_name=_('Student'), on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(_('Enrollment Date'), auto_now_add=True)

class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student,verbose_name=_("Student"), on_delete=models.CASCADE, related_name='requests')
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE, related_name='requests')
    status = models.CharField(verbose_name=_("Status"), max_length=50, choices=STATUS_CHOICES, default="Pending")
    request_date = models.DateTimeField(verbose_name=_("Request Date"), auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.student} - {self.course}'
    
    def save(self):
        exist = Enrollment.objects.filter(Q(student=self.student) & Q(course=self.course)).exists()
        if self.status == "Approved" and not exist :
            Enrollment.objects.create(
                student = self.student,
                course = self.course
            )
        return super().save()

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    read = models.BooleanField(verbose_name=_("Read"), default=False)

