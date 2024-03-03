from django.shortcuts import render


def index(request):

    person = [
        {"name" : "abhi", "age" : 22},
        {"name" : "ravi", "age" : 29},
        {"name" : "kbhi", "age" : 21},
        {"name" : "hari", "age" : 27},
        {"name" : "abha", "age" : 25},
        ]


    return render (request, "index.html",  context = {'person': person})


# def confirm(request):
#     return HttpResponse("<h1>your program is confirm to run</h1>")