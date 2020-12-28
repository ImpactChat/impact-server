from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hi(request):
    return HttpResponse("""{
        "associatedApplications": [
            {
            "applicationId": "257171a6-e380-4fb5-8722-9e465f856c29"
            }
        ]
        }""")
