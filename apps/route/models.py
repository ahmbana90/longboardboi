from django.db import models
from apps.inheritme.models import CreatedModifiedAtDatetime

class Route(CreatedModifiedAtDatetime):
    LEVEL_CHOICES = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
    )
    uploader = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    tags = models.ManyToManyField("route.Tag",through="RouteTag")
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES)
    
    def all_tags(self):
        return ", ".join([tag.tag_name for tag in self.tags.all()])
    
    def __str__(self):
        return self.title
    
    
    
class Tag(CreatedModifiedAtDatetime):
    TAG_CHOICES=(
        ("chill","chill"),
        ("no traffic","no traffic"),
        ("good tar","good tar"),
        ("bad tar","bad tar"),
        ("scenic","scenic"),
        ("urban","urban"),
        ("no elevation","no elevation"),
        ("strong elevation","strong elevation"),
        ("in nature","in nature"),
        ("short","short"),
        ("long","long"),
        ("multiple days","multiple days"),
        ("downhill", "downhill"),  
    )
    
    tag_name=models.CharField(max_length=50,choices=TAG_CHOICES)
    
    def __str__(self):
        return self.tag_name
    
class RouteTag(CreatedModifiedAtDatetime):
    modified_at = None
    tag_id = models.ForeignKey("route.Tag", on_delete=models.CASCADE)
    route_id = models.ForeignKey("route.Route", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                "route_id",
                "tag_id",
                name="route_tag_unique",
                violation_error_message=f"Tag already exists for route!",
            )
        ]
        
    @property
    def title(self):
        return self.route_id.title
    @property
    def tag(self):
        return self.tag_id.tag_name
