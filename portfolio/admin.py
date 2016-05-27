from django.contrib import admin

# import model
from portfolio.models import Project, ProjectImage, Product, Category, Faq, Page, Slider

class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_display = ('title', 'subtitle')

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'short_description', 'start_date',)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'slug', 'created', 'updated')
    # list_filter = ('created', 'updated')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image',)
    list_display_links = ('project',)

class FaqImageAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer',)

class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ('title', 'slug', 'status', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Faq, FaqImageAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Slider, SliderAdmin)
