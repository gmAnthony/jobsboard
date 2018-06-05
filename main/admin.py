from django.contrib import admin
from main.models import Job, Retweeter

class JobAdmin(admin.ModelAdmin):
    list_display = ('approved', 'spam', 'filled', 'title', 'contact_email', "posted_from_ip")
    list_display_links = ('title',)
    list_filter = ('approved', 'filled', 'spam')

admin.site.register(Job, JobAdmin)


class RetweeterAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_display_links = ('username',)

admin.site.register(Retweeter, RetweeterAdmin)