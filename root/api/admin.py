from django.contrib import admin

from .models import Category,Book

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Book)
class bookadmin(admin.ModelAdmin):
    list_display = ['title',]