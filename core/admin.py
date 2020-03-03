from django.contrib import admin

# Register your models here.
from .models import Book, Category, Favorite


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Book)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorite)
