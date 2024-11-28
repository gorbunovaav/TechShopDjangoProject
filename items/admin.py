from django.contrib import admin

from items.models import Categories, Item

# admin.site.register(Categories)
# admin.site.register(Item)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

