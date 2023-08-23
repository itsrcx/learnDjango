from django.contrib import admin
from blogging import models

class PostAdmin(admin.ModelAdmin):
    list_display =('title','slug','status','created_on')
    list_filter = ('status',)
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(models.Post, PostAdmin)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post','created_on','active')
    list_filter = ('active','created_on')
    search_fields = ('name', 'email','body')
    actions = ['approve_comments']

    def approve_comments(self,request, queryset):
        queryset.update(active=True)


