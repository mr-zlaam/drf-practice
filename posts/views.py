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
    return
