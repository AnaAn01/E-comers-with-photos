from django.contrib import admin
from home.models import Item


class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
