from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import *
# Register your models here.

admin.site.register(FAQ)
admin.site.register(CreatorDetail)
admin.site.register(Contact)
admin.site.register(Perk)
admin.site.register(Content)
admin.site.register(Stat)
admin.site.register(WorkHistory)
admin.site.register(YouTubeVideo)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_items_in_each_category')

    def number_of_items_in_each_category(self, obj):
        count = Activity.objects.filter(category=obj).count()
        
        url = (
            reverse('admin:app_activity_changelist')#Assuming the app after admin: is called 'app'
            + f'?category__id__exact={obj.id}'
        )
        return format_html('<a href="{}">{}</a>', url, count)

    number_of_items_in_each_category.short_description = 'Number of Activities'

    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'location', 'latitude', 'longitude', 'category', 'updated_at')

    """
    def items_per_category(self, obj):
        count = Activity.objects.filter(category=obj.category).count()
        
        url = (
            reverse('admin:app_activity_changelist')#Assuming the app after admin: is called 'app'
            + f'?activity__id__exact={obj.id}'
        )
        #return format_html('<a href="{}">{}</a>', url, count)
        
        return count

    items_per_category.short_description = 'Number of Items'
    """
