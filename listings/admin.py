from django.contrib import admin
from .models import Category,Product,Review

admin.site.site_header = "SOKOyetu"
admin.site.site_title = "SOKOyetu Admin"
admin.site.index_title = "Welcome to SOKOyetu Adminstration"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','slug','price','available')
    list_filter = ('category','available')
    prepopulated_fields = {'slug': ('name',)}

    inlines = [ReviewInline]
