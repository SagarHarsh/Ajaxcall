from django.shortcuts import render
from django.http import HttpResponse
from app1.models import DB_save
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def demo_ajax(request):

    return render(request,"ajax.html")


def Save_DB(request):
    no=request.POST.get("t1")
    name=request.POST.get("t2")
    contact=request.POST.get("t3")
    email=request.POST.get("t4")

    DB_save(no=no,name=name,contact=contact,email=email).save()

    return HttpResponse("Data are Saved")

@csrf_exempt
def validate(request):
    try:

        DB_save.objects.get(email=request.POST.get("EM"))
        return JsonResponse({"result":True})
    except DB_save.DoesNotExist:
        return JsonResponse({"result": False})


