from django.shortcuts import render
from django.db.models import Avg

from .models import Route, RouteTag
from apps.rating.models import Rating



def route_detail(request,id):
    route = Route.objects.get(pk=id)
    avg_rate = Rating.objects.filter(route_id=id).aggregate(avg_rating=Avg("rating"))["avg_rating"]
    route_tags = RouteTag.objects.filter(route_id=id)

    context = {
        "route":route,
        "avg_rate":avg_rate,
        "route_tags":route_tags
    }
    
    return render(request, 'route/route_detail.html', context)