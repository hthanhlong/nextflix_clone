from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view()
def login(request):
    return Response({"message": "Hello, world!"})

@api_view()
def signup(request):
    return Response({"message": "Hello, world!"})
