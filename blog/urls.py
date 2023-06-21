from django.urls import path
from . import views


urlpatterns = [
    # loacalhost:8080/
    path('', views.post_list, name='post_list'),
    # localhost:8080/post/5
    path('post/<int:pk>/', views.post_detail, name='post_detail_test')
]