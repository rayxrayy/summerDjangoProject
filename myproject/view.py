from django.http import HttpResponse
def home(request):
    return HttpResponse("hello")
    return HttpResponse("nothing")