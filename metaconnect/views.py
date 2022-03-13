from django.shortcuts import render
from django.shortcuts import redirect
import requests

from metaconnect.models import Owner,ProjectDetails

# Create your views here.
def Home(request):

    return render(request,'home.html')


def checkMe(request):
    print('Helloooo')

    if request.POST:
        address =request.POST.get('address')
        moralisid =request.POST.get('user')
        project =request.POST.get('nftname')
        symbol =request.POST.get('symbol')
        desc =request.POST.get('desc')
        myfile  = request.FILES['allimages'] 
        print(myfile)
        
        try:
            ownerobj =  Owner.objects.get(owneraddress=address)
        except:
            ownerobj = Owner()
            ownerobj.owneraddress=address
            ownerobj.moralisid=moralisid
            ownerobj.save()
        temp = ProjectDetails()
        temp.user=ownerobj
        temp.name= project
        temp.symbol = symbol
        temp.description=desc
        temp.image = myfile
        temp.save()
    
    return render(request,'user_page.html')