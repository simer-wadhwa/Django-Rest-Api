from django.shortcuts import HttpResponse
from django.http import JsonResponse

def home_page(request):
    print("home page request")
    friends=['asd','sdg','jkd']
    #return HttpResponse("<h1>This is home page</h1>")
    return JsonResponse(friends , safe=False)
