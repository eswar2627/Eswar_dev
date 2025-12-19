from django.contrib import admin
from django.utils.html import format_html

from .models import Project, ProjectImage, Contact, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
    ordering = ('category',)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ('image_preview',)
    fields = ('image', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="120" style="border-radius:6px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]

    list_display = (
        'title',
        'backend',
        'frontend',
        'database',
        'deployment',
        'created_at',
    )

    search_fields = (
        'title',
        'backend',
        'frontend',
        'database',
    )

    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
