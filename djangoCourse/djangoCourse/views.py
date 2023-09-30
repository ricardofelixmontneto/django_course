from django.http import HttpResponse
import json

# FUNCTION-based views
def home(request):
    return HttpResponse('Hello world!')
