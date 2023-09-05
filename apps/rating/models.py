from django.db import models
from apps.inheritme.models import CreatedModifiedAtDatetime

class Rating(CreatedModifiedAtDatetime):
    RATING_CHOICES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    rating=models.IntegerField()
    route_id=models.ForeignKey("route.Route", on_delete=models.CASCADE)    
    user_id=models.ForeignKey("user.User", on_delete=models.CASCADE)
    rating_text=models.TextField()
    cat_fit_rat=models.CharField(max_length=1,choices=RATING_CHOICES)
    lev_fit_rat=models.CharField(max_length=1,choices=RATING_CHOICES)
