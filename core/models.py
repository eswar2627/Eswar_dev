from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    backend_implementation = models.TextField(blank=True)
    frontend_implementation = models.TextField(blank=True)
    why_this_application = models.TextField(blank=True)
    backend = models.CharField(max_length=200)
    frontend = models.CharField(max_length=200)
    database = models.CharField(max_length=200)
    features = models.TextField(blank=True)
    deployment = models.CharField(max_length=200)
    payment = models.CharField(max_length=200, blank=True)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='images',
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to='projects/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'webp']
            )
        ]
    )

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"{self.project.title} Image"


class Skill(models.Model):
    category = models.CharField(max_length=100)
    skills = models.TextField(help_text="Comma-separated skills")

    def __str__(self):
        return self.category


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"
