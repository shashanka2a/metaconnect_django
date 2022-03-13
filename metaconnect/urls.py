from django.urls import path,include
from metaconnect.views import Home,checkMe
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('',Home,name='home'),
    path('check/',checkMe,name='checkme')


]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
