from django.urls import path
from  . import views 
from .views import PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    
    path('home',views.home,name='home'),
    
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('detail/<slug:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


]
