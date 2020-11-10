from django.contrib import admin
from .models import Bitcoin


class BitcoinAdmin(admin.ModelAdmin):
    list_display = ("price", "last_updated")


admin.site.register(Bitcoin, BitcoinAdmin)
