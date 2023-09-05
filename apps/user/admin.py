from django.contrib import admin
from apps.user.models import User



class CustomUser(admin.ModelAdmin):
    fieldsets = (
        (None,{"fields":("username","first_name","last_name","bio","date_of_birth","email")}),
    )
    
    list_display = (
        "username",
        "get_created_at",
        "get_uploaded_routes",
        "first_name",
        "last_name",
    )
    
    @admin.display(description="Date of registration")
    def get_created_at(self,obj):
        return obj.date_joined
    
    @admin.display(description="Number of routes uploaded")
    def get_uploaded_routes(self,obj):
        return obj.get_routes_uploaded
    

admin.site.register(User,CustomUser)