from django.shortcuts import render
from django.shortcuts import redirect
import requests

from metaconnect.models import Owner,ProjectDetails

# Create your views here.
def Home(request):

    return render(request,'home.html')


def validate(request):

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
    project =  ProjectDetails.objects.get(user=userwallet)
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
    headers={"Authorization": 'fec94101-bb38-44ae-bd6f-0f0c591070fd'},
    files={"file": file}
    )
    
    print(type(response))
    x = response.json()
    contract  = getData()
    contract=contract.replace('_newuri',"'"+x['ipfs_url']+"'")
    contract=contract.replace('MyToken',project.name)

    print(x['error'])
    
    

    return render(request,'output.html',{'contract':contract,'userwallet':userwallet,'project':project,'response':x['response'], 'ipfs_url':x['ipfs_url'],'file_name':x['file_name'],'error':x['error']}   )


def deploy(request,address):
    userwallet  = Owner.objects.get(owneraddress=address)
    project=ProjectDetails.objects.get(user=userwallet)
    url = "https://api.nftport.xyz/v0/contracts"
    payload = "{\n  \"chain\": \"polygon\",\n  \"name\": \"CRYPTOPUNKS\",\n  \"symbol\": \"CYBER\",\n  \"owner_address\":wallet,\n  \"metadata_updatable\": false,\n  \"type\": \"erc1155\"\n}"
    print(project.name)
    print(project.symbol)
    payload = payload.replace('CRYPTOPUNKS',project.name)
    payload = payload.replace('CYBER',project.symbol)
    payload=payload.replace('wallet','"'+address+'"')

    headers = {
    'Content-Type': "application/json",
    'Authorization': "fec94101-bb38-44ae-bd6f-0f0c591070fd"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response)
    return render(request,'deploy.html',{'respose':response.text})

def getData():
    return '''
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.4;

        import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
        import "@openzeppelin/contracts/access/Ownable.sol";

        contract MyToken is ERC1155, Ownable {
            constructor() ERC1155("") {}

            function setURI(string memory newuri) public onlyOwner {
                _setURI(_newuri);
            }

            function mint(address account, uint256 id, uint256 amount, bytes memory data)
                public
                onlyOwner
            {
                _mint(account, id, amount, data);
            }

            function mintBatch(address to, uint256[] memory ids, uint256[] memory amounts, bytes memory data)
                public
                onlyOwner
            {
                _mintBatch(to, ids, amounts, data);
            }
        }
    '''
