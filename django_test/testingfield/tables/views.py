from django.shortcuts import render

# Create your views here.
 
def tabs(request):
    person = [
        {"name" : "abhi", "age" : 22},
        {"name" : "ravi", "age" : 19},
        {"name" : "kbhi", "age" : 21},
        {"name" : "hari", "age" : 17},
        {"name" : "abha", "age" : 25},
        ]
    
    return render(request, "index.html", context={'person':person})

def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
