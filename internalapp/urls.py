from django.urls import path
from . import views


urlpatterns = [

    path("",views.home,name = "homepage"),
    path("result",views.welcome,name = "welcome"),
    path("users",views.users,name = "users"),
    path("graph",views.graph,name = "users"),


]