from django.contrib import admin

# import model
from .models import Project, ProjectImage, Category


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'short_description', 'start_date',)
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image',)
    list_display_links = ('project',)


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(Category, CategoryAdmin)
