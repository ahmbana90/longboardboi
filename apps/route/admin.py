from django.contrib import admin
from apps.route.models import Route, Tag,RouteTag
from .forms import RouteAdminForm

class CustomTag(admin.ModelAdmin):
    list_display = ('tag_name',)
    

class CustomRoute(admin.ModelAdmin):
    form = RouteAdminForm
    list_display = (
        "title",
        "uploader",
        "level",
        "get_tags",
        "location",
        "get_description",
    )
    
    @admin.display(description="tags")
    def get_tags(self,obj):
        return ", ".join([tag.tag_name for tag in obj.tags.all()])

    @admin.display(description="description")
    def get_description(self,obj):
        return obj.description[:50]+"..."
    
    
class CustomRouteTag(admin.ModelAdmin):
    list_display = (
        "title",
        "tag"
    )
    

admin.site.register(Tag, CustomTag)
admin.site.register(Route,CustomRoute)
admin.site.register(RouteTag,CustomRouteTag)



