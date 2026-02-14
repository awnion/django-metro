from django.contrib import admin

from .models import Metro, MetroLine


class MetroAdminInline(admin.StackedInline):
    model = Metro
    extra = 0
    list_display = ("title", "line")
    list_display_links = ("title",)
    list_filter = ("title", "line")
    search_fields = ("title",)


class MetroLineAdmin(admin.ModelAdmin):
    inlines = [MetroAdminInline]
    list_display = ("number", "title", "get_admin_color")
    list_display_links = ("number", "title", "get_admin_color")
    list_filter = ("number", "title")
    search_fields = ("number", "title")


admin.site.register(MetroLine, MetroLineAdmin)
