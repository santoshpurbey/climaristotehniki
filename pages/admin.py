from django.contrib import admin

from .models import Faq, Page, Slider, Category
# Register your models here.


class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_display = ('title', 'subtitle')

class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'category',)

class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ('title', 'slug', 'status', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}

class  CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Faq, FaqAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Category, CategoryAdmin)
