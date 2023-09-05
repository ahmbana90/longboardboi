from django.db import models
from apps.inheritme.models import CreatedModifiedAtDatetime

class ProfilePicture(CreatedModifiedAtDatetime):
    user_id=models.ForeignKey("user.User", on_delete=models.CASCADE)
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return f"Profile Picture for "
    
class RoutePicture(CreatedModifiedAtDatetime):
    route_id=models.ForeignKey("route.Route", on_delete=models.CASCADE)
    pic=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
class RouteVideo(CreatedModifiedAtDatetime):
    route_id=models.ForeignKey("route.Route", on_delete=models.CASCADE)
    vid=models.FileField(upload_to=None, max_length=100)
    
class DekoPic(CreatedModifiedAtDatetime):
    pass