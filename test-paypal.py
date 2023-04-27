import os
import requests
import json
from dotenv import load_dotenv
os.environ['PYTHON_FUTURE_FSTRING_WIDTH'] = '200'


load_dotenv()
SANDBOX_CLIENT_ID = os.environ.get('SANDBOX_CLIENT_ID')
SANDBOX_CLIENT_SECRET = os.environ.get('SANDBOX_CLIENT_SECRET')
SANDBOX_ACCESS_TOKEN = os.environ.get('SANDBOX_ACCESS_TOKEN')
SANDBOX_PRODUCT_ID = os.environ.get('SANDBOX_PRODUCT_ID')


headers = {
    'Authorization': f'Bearer {SANDBOX_ACCESS_TOKEN}',
    'X-PAYPAL-SECURITY-CONTEXT': '{"consumer":{"accountNumber":1181198218909172527,"merchantId":"5KW8F2FXKX5HA"},"merchant":{"accountNumber":1659371090107732880,"merchantId":"2J6QB8YJQSJRJ"},"apiCaller":{"clientId":"AdtlNBDhgmQWi2xk6edqJVKklPFyDWxtyKuXuyVT-OgdnnKpAVsbKHgvqHHP","appId":"APP-6DV794347V142302B","payerId":"2J6QB8YJQSJRJ","accountNumber":"1659371090107732880"},"scopes":["https://api-m.paypal.com/v1/subscription/.*","https://uri.paypal.com/services/subscription","openid"]}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    # 'PayPal-Request-Id': 'PRODUCT-18062019-001',
    'Prefer': 'return=representation',
}

def get_access_token():
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en_US',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')
    url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'
    response = requests.post(url, auth=(client_id, client_secret), headers=headers,data=data)
    if response.status_code == 200:
        access_token = response.json()['access_token']
        print('Access Token:', access_token)
    else:
        print('Error:', response.status_code, response.text)

def create_product(headers):
    data = '{ "name": "Video Streaming Service", "description": "Video streaming service", "type": "SERVICE", "category": "SOFTWARE", "image_url": "https://example.com/streaming.jpg", "home_url": "https://example.com/home" }'
    response = requests.post('https://api-m.sandbox.paypal.com/v1/catalogs/products', headers=headers, data=data)


def create_plan(headers:dict,product_id:str,name:str,description:str,price:str,interval_unit:str,interval_count:int):
    # Template
    # data = '{ "product_id": "PROD-126180201M064221R", "name": "Basic", "description": "Basic", "status": "ACTIVE", "billing_cycles": [ { "frequency": { "interval_unit": "MONTH", "interval_count": 1 }, "tenure_type": "TRIAL", "sequence": 1, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "3", "currency_code": "USD" } } }, { "frequency": { "interval_unit": "MONTH", "interval_count": 1 }, "tenure_type": "TRIAL", "sequence": 2, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "6", "currency_code": "USD" } } }, { "frequency": { "interval_unit": "MONTH", "interval_count": 1 }, "tenure_type": "REGULAR", "sequence": 3, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "10", "currency_code": "USD" } } } ], "payment_preferences": { "auto_bill_outstanding": true, "setup_fee": { "value": "10", "currency_code": "USD" }, "setup_fee_failure_action": "CONTINUE", "payment_failure_threshold": 3 }, "taxes": { "percentage": "10", "inclusive": false } }'
    # Annual
    # data = '{ "product_id": "PROD-126180201M064221R", "name": "Annual", "description": "Annual", "status": "ACTIVE", "billing_cycles": [ { "frequency": { "interval_unit": "YEAR", "interval_count": 1 }, "tenure_type": "REGULAR", "sequence": 1, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "1200", "currency_code": "USD" } } } ], "payment_preferences": { "auto_bill_outstanding": true,  "setup_fee_failure_action": "CONTINUE", "payment_failure_threshold": 3 },  }'
    # Semi-Annual
    # data = '{ "product_id": "PROD-126180201M064221R", "name": "Semi-Annual", "description": "Semi_Annual", "status": "ACTIVE", "billing_cycles": [ { "frequency": { "interval_unit": "MONTH", "interval_count": 6 }, "tenure_type": "REGULAR", "sequence": 1, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "750", "currency_code": "USD" } } } ], "payment_preferences": { "auto_bill_outstanding": true,  "setup_fee_failure_action": "CONTINUE", "payment_failure_threshold": 3 } }'
    # Monthly
    data = f'{{ "product_id": "{product_id}", "name": "{name}", "description": "{description}", "status": "ACTIVE", "billing_cycles": [{{ "frequency": {{ "interval_unit": "{interval_unit}", "interval_count": "{interval_count}" }}, "tenure_type": "REGULAR", "sequence": 1, "total_cycles": 0, "pricing_scheme": {{ "fixed_price": {{ "value": "{price}", "currency_code": "USD" }} }} }}], "payment_preferences": {{ "auto_bill_outstanding": true,  "setup_fee_failure_action": "CONTINUE", "payment_failure_threshold": 3 }} }}'

    # data_dict = json.loads(data)
    response = requests.post('https://api-m.sandbox.paypal.com/v1/billing/plans', headers=headers, data=data)
    return response


def list_plans(headers):
    response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/plans', headers=headers)
    return response.json()

# create_plan(headers=headers,
#             product_id=SANDBOX_PRODUCT_ID,
#             name="Semi-Annual",
#             description="Semi-Annual subscription",
#             price="750",
#             interval_unit="MONTH",
#             interval_count=6)
plans=list_plans(headers=headers)['plans']
for plan in plans:
    print(plan['id']+' '+plan['name'])