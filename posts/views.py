from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse


# Create your views here.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
@api_view(http_method_names=["POST", "GET"])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        res = {
            "message": "OK",
            "success": True,
            "status": status.HTTP_201_CREATED,
            "data": data,
        }
        return Response(data=res, status=status.HTTP_201_CREATED)
    return HttpResponse("Hello world")


@api_view(http_method_names=["GET"])
def list_posts(request: Request):
    posts = [
        {"id": 1, "name": "John Doe", "age": 30},
        {"id": 2, "name": "Jane Smith", "age": 25},
        {"id": 3, "name": "Bob Johnson", "age": 40},
        {"id": 4, "name": "Alice Brown", "age": 28},
        {"id": 5, "name": "Mike Davis", "age": 35},
        {"id": 6, "name": "Emily Taylor", "age": 22},
        {"id": 7, "name": "Sarah Lee", "age": 32},
        {"id": 8, "name": "Kevin White", "age": 45},
        {"id": 9, "name": "Lisa Hall", "age": 38},
        {"id": 10, "name": "Tom Harris", "age": 42},
    ]
    return Response(data=posts, status=status.HTTP_200_OK)
