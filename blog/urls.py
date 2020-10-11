from django.urls import path
from  . import views 
from .views import PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('courses/',views.courses,name='courses'),
    path('index1/',views.index1,name='index1'),  
    path('single/',views.single,name='single'),  

    
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('detail/<slug:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


]
