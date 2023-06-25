from django.contrib import admin
from blogging import models

class PostAdmin(admin.ModelAdmin):
    list_display =('title','slug','status','created_on')
    list_filter = ('status',)
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(models.Post, PostAdmin)
