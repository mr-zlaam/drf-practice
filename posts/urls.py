from django.urls import path
from posts.views import homepage


urlpatterns = [path("home/", homepage, name="posts_home")]
