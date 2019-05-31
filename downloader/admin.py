from django.contrib import admin
from .models import Request

class HistoryAdmin(admin.ModelAdmin):
    readonly_fields = ("url", 'date')

admin.site.register(Request, HistoryAdmin)