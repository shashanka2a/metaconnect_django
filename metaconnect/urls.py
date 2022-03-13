from django.urls import path,include
from metaconnect.views import Home,checkMe,FormView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('',Home,name='home'),
    path('checkMe/',checkMe,name='checkme'),
    path('user/<str:addr>/',FormView,name='formview')


]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
