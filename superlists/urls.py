from django.urls import path  
from lists.views import home_page,about_page  

urlpatterns = [
    path("", home_page, name="home"),  
    path("about/", about_page,name="about")
]