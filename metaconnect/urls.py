from django.urls import path,include
from metaconnect.views import Home,checkMe,Dashboard,upload,deploy
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('',Home,name='home'),
    path('check/',checkMe,name='checkme'),
    path('dashboard/<str:address>/',Dashboard,name='dashboard'),
    path('upload/<str:address>/',upload,name='upload'),
    path('deploy/<str:address>/',deploy,name='deploy')



]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
