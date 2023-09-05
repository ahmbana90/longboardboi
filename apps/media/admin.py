from django.contrib import admin

from apps.media.models import ProfilePicture,RoutePicture,RouteVideo

admin.site.register(ProfilePicture)
admin.site.register(RoutePicture)
admin.site.register(RouteVideo)