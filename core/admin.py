from django.contrib import admin
from django.utils.html import format_html

from .models import Project, ProjectImage, Contact, Skill


# =========================
# Skill Admin
# =========================
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
    ordering = ('category',)


# =========================
# Project Image Inline (with preview)
# =========================
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ('image_preview',)
    fields = ('image', 'image_preview')

    def image_preview(self, obj):
        if not obj or not obj.image:
            return "No Image"
        return format_html(
            '<img src="{}" width="120" style="border-radius:6px;" />',
            obj.image.url,
        )

    image_preview.short_description = "Preview"


# =========================
# Project Admin
# =========================
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


# =========================
# Contact Admin
# =========================
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
