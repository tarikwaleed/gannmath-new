import datetime
import math
from allauth.account.views import SignupView as AllauthSignupView, LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from registration.models import Subscription
import os
from dotenv import load_dotenv,find_dotenv
from django.views.decorators.csrf import csrf_exempt
load_dotenv()
load_dotenv(find_dotenv(), override=True)


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
            subscription = request.user.subscription
            if subscription.is_active:
                return render(request, "our_service.html")
            else:
                return render(request, "home.html", {"message": "Please subscribe to access our service."})
        except Subscription.DoesNotExist:
            return render(request, "home.html", {"message": "Please subscribe to access our service."})


class MonthlySubscriptionView(LoginRequiredMixin, View):
    def get(self, requst):
        plan_id=os.environ.get('LIVE_MONTHLY_PLAN_ID')
        client_id=os.environ.get('LIVE_CLIENT_ID')
        context={
            'plan_id':plan_id,
            'client_id':client_id
        }
        return render(requst, "monthly_subscription.html",context=context)

class AnnualSubscriptionView(LoginRequiredMixin,View):
    def get(self, requst):
        plan_id=os.environ.get('LIVE_ANNUAL_PLAN_ID')
        client_id=os.environ.get('LIVE_CLIENT_ID')
        context={
            'plan_id':plan_id,
            'client_id':client_id
        }
        return render(requst, "annual_subscription.html",context=context)
class SemiAnnualSubscriptionView(LoginRequiredMixin,View):
    def get(self, requst):
        plan_id=os.environ.get('LIVE_SEMI_ANNUAL_PLAN_ID')
        client_id=os.environ.get('LIVE_CLIENT_ID')
        context={
            'plan_id':plan_id,
            'client_id':client_id
        }
        return render(requst, "semi_annual_subscription.html",context=context)

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
