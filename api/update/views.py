from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update as UpdateModel

# Create your views here.
def update_model_detail_view(request):
    data = {
        "count": 1000,
        "content": 'Nothing to show'
    }
    return JsonResponse(data)