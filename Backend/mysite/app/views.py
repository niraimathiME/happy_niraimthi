from django.shortcuts import render
import json
from django.http import JsonResponse
from .mongodb import client, db, collection
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def test_mongodb(request):
    try:
        client.admin.command("ping")

        return JsonResponse({
            "status": "success",
            "database": db.name,
            "collection": collection.name
        })

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        })
    