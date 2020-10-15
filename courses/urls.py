from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
   path('about/',views.about,name='about'),
    path('courses/',views.courses,name='courses'),
    path('',views.index1,name='index1'),  
    path('single/',views.single,name='single'),  

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
