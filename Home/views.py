from django.shortcuts import render

# Create your views here.
def homepage(request):
    
    information = {
        "name" : "Hexacore.inc",
        "location":"Baglung",
        "established":"2002",
        "copyright":"2024"  
    }
    
    contact = {
        "phone" : "98xxxxxxxx",
        "email":"hexacore@support.com",
        "tel":"061-522456"
    }
    details = {
        "info" : information,
        "contact":contact,
    }
    return render(request,'Home/index.html', details)

def aboutpage(request):
    return render(request, 'Home/about.html')