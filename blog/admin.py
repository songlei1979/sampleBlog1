from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Profile, Comment

class PostUnderCategory(admin.TabularInline):
    model = Post
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name']
    inlines = [PostUnderCategory]

class PostAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Comment)