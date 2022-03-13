from django.shortcuts import render
from django.shortcuts import redirect

from metaconnect.models import Owner,ProjectDetails

# Create your views here.
def Home(request):

    return render(request,'home.html')


def checkMe(request):
    print('Helloooo')
    print(request.GET.get('user'))
    print(request.GET.get('wallet'))
    if request.GET:
        address =request.GET.get('wallet')
        moralisid =request.GET.get('user')
        print(address)
        ownerobj =  Owner.objects.get(owneraddress=address)
        if ownerobj:
            redirect('formview',address)
        else:
            owner = Owner()
            owner.owneraddress=address
            owner.moralisid=moralisid
            owner.save()
            redirect('formview',address)

    return render(request,'home.html')


def FormView(request,addr):
    
    return render(request,'user_page.html')
