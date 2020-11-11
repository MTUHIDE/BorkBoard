from django.contrib import admin
from .models import CatalogItem, Category, SubCategory
from accountant.models import user_profile
from profanity_check.models import ArchivedType

# Register your models here.
class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['category_name']}),
        ('Date information', {'fields': ['date_added'], 'classes': ['collapse']}),
    ]
    list_display = ('date_added', 'category_name')
    list_filter = ['date_added', 'date_updated']
    inlines = [SubCategoryInline]

class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ('reported', 'archived', 'archivedType', 'pk', 'date_added', 'username', 'item_price', 'item_title', 'item_description')
    list_filter = ['reported', 'archived', 'category', 'date_added', 'username']
    search_fields = ['item_title', 'item_description']
    actions = ['remove_post', 'allow_post', 'ignore_post', ]

    def remove_post(self, request, queryset):
        queryset.update(reported=False)
        queryset.update(archived=True)
        queryset.update(archivedType=ArchivedType.Types.REMOVED)
        # Decrement number of points by three
        profile = user_profile.objects.get(user = request.user)
        profile.points = profile.points - 3
        profile.save()
    remove_post.short_description = "Remove offending posts"

    def allow_post(self, request, queryset):
        queryset.update(reported=False)
        queryset.update(archived=False)
        queryset.update(archivedType=ArchivedType.Types.VISIBLE)
    allow_post.short_description = "Unarchive: mark acceptable"

    def ignore_post(self, request, queryset):
        queryset.update(reported=False)
    ignore_post.short_description = "Ignore report (don't use this, unarchive instead)"

    def get_actions(self, request):
        #https://stackoverflow.com/questions/34152261/remove-the-default-delete-action-in-django-admin
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions




admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CatalogItem, CatalogItemAdmin)
