import math
import requests
from allauth.account.views import SignupView as AllauthSignupView, LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import os
from dotenv import load_dotenv,find_dotenv
from django.views.decorators.csrf import csrf_exempt
import json

from registration.models import Subscription
load_dotenv()
load_dotenv(find_dotenv(), override=True)

GEX_BOT_API_KEY = os.environ.get("GEX_BOT_API_KEY")
BASE_URL = "https://api.gexbot.com/spx"


class SignupView(AllauthSignupView):
    template_name = "account/signup.html"


class LoginView(LoginView):
    template_name = "account/login.html"


class LogoutView(LogoutView):
    template_name = "account/logout.html"


class HomePageView(TemplateView):
    template_name = "home.html"


class OurServiceView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            subscription = Subscription.objects.get(user=request.user)
            if subscription.status == 'COMPLETED':
                return render(request, "our_service.html")
            else:
                return render(request, "home.html", {"message": "Please subscribe to access our service."})
        except Subscription.DoesNotExist:
            return render(request, "home.html", {"message": "Please subscribe to access our service."})

class MonthlySubscriptionView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get('ENVIRONMENT')
        if environment == 'live':
            plan_id = os.environ.get('LIVE_MONTHLY_PLAN_ID')
            client_id = os.environ.get('LIVE_CLIENT_ID')
        else:
            plan_id = os.environ.get('SANDBOX_MONTHLY_PLAN_ID')
            client_id = os.environ.get('SANDBOX_CLIENT_ID')
        
        context = {
            'plan_id': plan_id,
            'client_id': client_id
        }
        return render(request, "monthly_subscription.html", context=context)

class MonthlyStandardCheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get('ENVIRONMENT')
        if environment == 'live':
            client_id = os.environ.get('LIVE_CLIENT_ID')
        else:
            client_id = os.environ.get('SANDBOX_CLIENT_ID')
        
        context = {
            'client_id': client_id
        }
        return render(request, "monthly_standard_checkout.html", context=context)

class AnnualSubscriptionView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get('ENVIRONMENT')
        if environment == 'live':
            plan_id = os.environ.get('LIVE_ANNUAL_PLAN_ID')
            client_id = os.environ.get('LIVE_CLIENT_ID')
        else:
            plan_id = os.environ.get('SANDBOX_ANNUAL_PLAN_ID')
            client_id = os.environ.get('SANDBOX_CLIENT_ID')
        
        context = {
            'plan_id': plan_id,
            'client_id': client_id
        }
        return render(request, "annual_subscription.html", context=context)


class SemiAnnualSubscriptionView(LoginRequiredMixin, View):
    def get(self, request):
        environment = os.environ.get('ENVIRONMENT')
        if environment == 'live':
            plan_id = os.environ.get('LIVE_SEMI_ANNUAL_PLAN_ID')
            client_id = os.environ.get('LIVE_CLIENT_ID')
        else:
            plan_id = os.environ.get('SANDBOX_SEMI_ANNUAL_PLAN_ID')
            client_id = os.environ.get('SANDBOX_CLIENT_ID')
        
        context = {
            'plan_id': plan_id,
            'client_id': client_id
        }
        return render(request, "semi_annual_subscription.html", context=context)

class CalculateView(View):
    def post(self, request):
        x = float(request.POST.get('x'))
        y = float(request.POST.get('y'))
        slider_value = float(request.POST.get('slider'))
        z = None

        # Get the selected option's text value
        slider_options = {
            0: '0.001',
            1: '0.01',
            2: '0.1',
            3: '1',
            4: '10',
            5: '100',
            6: '1000',
        }
        if slider_value in slider_options:
            z = float(slider_options[slider_value])
        print(f'x: {x}')
        print(f'y: {y}')
        print(f'z: {z}')

        w = x * z
        r = y * z
        e = math.floor(abs(math.pow(w, 0.5) - math.pow(r, 0.5)) / 0.005555)
        print(f'e: {e}')
        
        a = 0

        if 43 <= e and e < 58:
            a = 45
        elif 58 <= e and e < 70:
            a = 60
        elif 70 <= e and e < 88:
            a = 72
        elif 88 <= e and e < 106:
            a = 90
        elif 106 <= e and e < 118:
            a = 108
        elif 118 <= e and e < 126.57:
            a = 120
        elif 126.57 <= e and e < 133:
            a = 128.57
        elif 133 <= e and e < 138:
            a = 135
        elif 138 <= e and e < 142:
            a = 140
        elif 142 <= e and e < 145.27:
            a = 144
        elif 145.27 <= e and e < 148:
            a = 147.27
        elif 148 <= e and e < 151.31:
            a = 150
        elif 151.31 <= e and e < 153.29:
            a = 152.31
        elif 153.29 <= e and e < 155:
            a = 154.29
        elif 155 <= e and e < 157.5:
            a = 156
        elif 157.5 <= e and e < 158.2:
            a = 157.5
        elif 158.2 <= e and e < 160:
            a = 158.82
        elif 160 <= e and e < 161.06:
            a = 160
        elif 161.06 <= e and e < 162:
            a = 161.05
        elif 162 <= e and e < 178:
            a = 162
        elif 178 <= e and e < 182:
            a = 180
        else:
            a = 1
        print(f'a: {a}')

        levels = [0.25, 0.383, 0.5, 0.618, 0.75, 1]
        cs = [(a * 4 * l) / 180 for l in levels]

        results = []
        for c in cs:
            if x / y > 1:
                results.append(round(math.pow(math.sqrt(w) - c, 2) / z, 5))
            else:
                results.append(round(math.pow(math.sqrt(w) + c, 2) / z, 5))
        arr = [1, 1.5278, 2, 2.4722, 3, 4]
        angles = [a * val for val in arr]       
        context = {
            'results': results,
            'angles': angles,
        }

        return render(request, 'our_service.html', context)







@csrf_exempt
def create_subscription(request):
    print('create_subscription view called')
    if request.method == 'POST':
        plan = request.POST.get('plan')
        order_id = request.POST.get('order_id')
        subscription_id = request.POST.get('subscription_id')
        payment_source = request.POST.get('payment_source')
        user = request.user
        print(f'DATA:{plan},{order_id},{subscription_id},{payment_source},{user}')
        
        
        subscription = Subscription.objects.create(
            user=user,
            plan=plan,
            order_id=order_id,
            subscription_id=subscription_id,
            payment_source=payment_source
        )
        subscription.save()
        print("subscription added to the database")
        
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

class GexBotAllFullView(LoginRequiredMixin,View):
    def get(self, request):
        url = f"{BASE_URL}/all/gex?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)


@csrf_exempt
def save_subscription(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        user=request.user
        subscription = Subscription(
            user=user,
            payment_id=payload['payment_id'],
            intent=payload['intent'],
            status=payload['status'],
            reference_id=payload['reference_id'],
            currency_code=payload['currency_code'],
            amount_value=payload['amount_value'],
            payee_email_address=payload['payee_email_address'],
            payee_merchant_id=payload['payee_merchant_id'],
            full_name=payload['full_name'],
            address_line_1=payload['address_line_1'],
            admin_area_2=payload['admin_area_2'],
            postal_code=payload['postal_code'],
            country_code=payload['country_code'],
            capture_id=payload['capture_id'],
            capture_status=payload['capture_status'],
            capture_amount_currency_code=payload['capture_amount_currency_code'],
            capture_amount_value=payload['capture_amount_value'],
            final_capture=payload['final_capture'],
            seller_protection_status=payload['seller_protection_status'],
            dispute_categories=json.loads(payload['dispute_categories']),
            create_time=payload['create_time'],
            update_time=payload['update_time'],
            payer_given_name=payload['payer_given_name'],
            payer_surname=payload['payer_surname'],
            payer_email_address=payload['payer_email_address'],
            payer_id=payload['payer_id'],
            payer_country_code=payload['payer_country_code'],
            links_href=payload['links_href'],
            links_rel=payload['links_rel'],
            links_method=payload['links_method']
        )
        subscription.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


class GexBotZeroFullView(LoginRequiredMixin,View):
    def get(self, request):
        url = f"{BASE_URL}/zero/gex?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)

class GexBotAllMajorsView(LoginRequiredMixin,View):
    def get(self, request):
        url = f"{BASE_URL}/all/majors?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)

class GexBotZeroMajorsView(LoginRequiredMixin,View):
    def get(self, request):
        url = f"{BASE_URL}/zero/majors?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)

class GexBotAllMaxView(LoginRequiredMixin,View):
    def get(self, request):
        url = f"{BASE_URL}/all/maxchange?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)

class GexBotZeroMaxView(LoginRequiredMixin,View):
    def get(self, request):
        url = f"{BASE_URL}/zero/maxchange?key={GEX_BOT_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data)

class SpxView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            subscription = Subscription.objects.get(user=request.user)
            if subscription.status == 'COMPLETED':
                context = {
                    'api_key': GEX_BOT_API_KEY
                }
                return render(request, "spx.html", context)
            else:
                return render(request, "home.html", {"message": "Please subscribe to access SPX."})
        except Subscription.DoesNotExist:
            return render(request, "home.html", {"message": "Please subscribe to access SPX."}) 