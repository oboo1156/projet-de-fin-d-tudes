from django.urls import path
from . import views

app_name = "counsel"
urlpatterns = [
   path('', views.home, name='home'),
   path('comment/<int:pk>', views.comment, name='comment'),
   path('create_story', views.create_story, name='create_story'),
   path('comment/comment_reply/<int:pk>', views.comment_reply, name='comment_reply'),
]
