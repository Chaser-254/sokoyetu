from django.contrib import admin
from .models import Category,Product,Review

class CustomAdminSite(admin.AdminSite):
    site_header = "sokoYETU"
    site_title = "sokoYETU Admin"
    index_title = "Welcome to sokoYETU Adminstration"

    def get_urls(self):
        urls  = super().get_urls()
        return urls
admin.site = CustomAdminSite()

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
