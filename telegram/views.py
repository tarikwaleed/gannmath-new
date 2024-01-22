import json
import requests
import os
from django.shortcuts import render, redirect
from django.views import View
from .models import TelegramGroup, SubActive
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST

# Create your views here.

class telegramView(TelegramGroup, View):
    def get(self, request):
        environment = os.environ.get("ENVIRONMENT")
        if environment == "live":
            plan_id = os.environ.get("LIVE_TELEGRAM_MONTHLY_PLAN_ID")
            client_id = os.environ.get("LIVE_CLIENT_ID")
        else:
            plan_id = os.environ.get("SANDBOX_TELEGRAM_MONTHLY_PLAN_ID")
            client_id = os.environ.get("SANDBOX_CLIENT_ID")

        context = {"plan_id": plan_id, "client_id": client_id}
        return render(request, "telegram_checkout.html", context=context)
        
class create_subActive(SubActive, View):
    @csrf_exempt
    def post(self, request):
        print("create subActive view called")
        if request.method == "POST":
            payload = json.loads(request.body)
            payer_fullname = payload.get("payer_fullname")
            is_planType = "Month"
            payID = payload.get("payID")
            total = payload.get("total")
            print(f"DATA: {payer_fullname}, {is_planType}, {payID}, {total}")

            subActive = SubActive.objects.create(
                is_planType=is_planType,
                payID=payID,
                total=total,
                is_active=False
            )
            ido = subActive.id
            print("subscription added to the database")
            #ids = SubActive.objects.filter("id")
            con = {
                "ido":ido,
                "payer_fullname":payer_fullname,
                "is_planType":is_planType,
                "payID":payID,
                "total":total,
            }
            context = json.dumps(con)
            return render(request, "form_subactive.html", {'context':context})
            #return HttpResponse(context)
            #return redirect(f"/form-subactive?ido={ido}&payer_fullname={payer_fullname}&is_planType={is_planType}&payID={payID}")
        else:
            return JsonResponse({"status": "error"})

            
@csrf_exempt
def save_telegram(request):
    if request.method == "POST":
        nameTelegram = request.POST.get("nameTelegram")
        IDs = SubActive.objects.get(payID=request.POST.get("payID"))
        is_planType = request.POST.get("is_planType")
        if is_planType == 'Month':
            dys = 30
        elif is_planType == '3 Months':
            dys = 90
        elif is_planType == '6 Months':
            dys = 180
        elif is_planType == 'one year':
            dys = 365
        else:
            dys = 0
        if IDs != '': 
            subActive = SubActive(
                endTime=datetime.now() + timedelta(days=dys),
                is_active=True,
                nameTelegram=nameTelegram
            )
            subActive.save(IDs)
        return render(request, "thanks.html")
        #return HttpResponse({"status": "success"})
    else:
        return HttpResponse({"status": "error", "message": "Invalid request method"})