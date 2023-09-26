from django.shortcuts import render
from django.views import View




class HomeView(View):
    template_name = "home/home.html"

    def get(self, request):
        context = {
            "menu_items": [
                {"title": "Profile", "url": "/profile/", "icon": "fa-solid fa-user"},
                {"title": "Home", "url": "/", "icon": "fa-solid fa-house"},
                {"title": "Search", "icon": "fa-solid fa-magnifying-glass"},
                {"title": "Settings", "icon": "fa-solid fa-gear"},
                ],
            }

        return render(request, self.template_name, {"menu_items": context["menu_items"]})