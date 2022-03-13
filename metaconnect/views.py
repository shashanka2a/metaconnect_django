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
    
    return redirect('dashboard',address)


def Dashboard(request,address):
    userwallet  = Owner.objects.get(owneraddress=address)

    project=ProjectDetails.objects.get(user=userwallet)
    print(project.image)


    return render(request,'user_page.html',{'walletdetails':userwallet,'project':project})
    

def upload(request,address):
    userwallet  = Owner.objects.get(owneraddress=address)
    project=ProjectDetails.objects.get(user=userwallet)
    path =str(project.image)
    file = open(path, "rb")
    print(file)
    response = requests.post(
    "https://api.nftport.xyz/v0/files",
    headers={"Authorization": 'd775b8ce-a5b7-420b-b818-3e7c46075ab2'},
    files={"file": file}
    )
    print('HWLLLLLLLLLLLLLLLLLLLL')
    print(type(response))
    x = response.json()
    print(x['response'])
    print(x['ipfs_url'])
    print(x['file_name'])
    print(x['error'])
    

    return render(request,'output.html',{'response':x['response'], 'ipfs_url':x['ipfs_url'],'file_name':x['file_name'],'error':x['error']}   )