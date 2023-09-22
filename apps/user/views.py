from django.shortcuts import render
from django.contrib.auth import login
from .models import User
from django.contrib.auth.forms import UserCreationForm
from apps.route.models import Route
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


def user_detail(request, id):
    user = User.objects.get(pk=id)
    routes_uploaded = Route.objects.filter(user_id=id).count()
    #profile picture
    
    
    
    context = {
        "user": user,
        "routes_uploaded": routes_uploaded
    }
    
    return render(request, "user/user_detail.html",context)


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "user/sign_up.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response