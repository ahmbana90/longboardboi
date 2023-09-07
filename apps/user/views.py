from django.shortcuts import render
from apps.user.models import User
from apps.route.models import Route

def user_detail(request, id):
    user = User.objects.get(pk=id)
    routes_uploaded = Route.objects.filter(user_id=id).count()
    #profile picture
    
    
    
    context = {
        "user": user,
        "routes_uploaded": routes_uploaded
    }
    
    return render(request, "user/user_detail.html",context)