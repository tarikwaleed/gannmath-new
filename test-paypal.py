import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
access_token = os.environ.get('PAYPAL_ACCESS_TOKEN')
product_id = os.environ.get('PRODUCT_ID')

headers = {
    'Authorization': f'Bearer {access_token}',
    'X-PAYPAL-SECURITY-CONTEXT': '{"consumer":{"accountNumber":1181198218909172527,"merchantId":"5KW8F2FXKX5HA"},"merchant":{"accountNumber":1659371090107732880,"merchantId":"2J6QB8YJQSJRJ"},"apiCaller":{"clientId":"AdtlNBDhgmQWi2xk6edqJVKklPFyDWxtyKuXuyVT-OgdnnKpAVsbKHgvqHHP","appId":"APP-6DV794347V142302B","payerId":"2J6QB8YJQSJRJ","accountNumber":"1659371090107732880"},"scopes":["https://api-m.paypal.com/v1/subscription/.*","https://uri.paypal.com/services/subscription","openid"]}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'PayPal-Request-Id': 'PRODUCT-18062019-001',
    'Prefer': 'return=representation',
}


def create_product(headers):
    data = '{ "name": "Video Streaming Service", "description": "Video streaming service", "type": "SERVICE", "category": "SOFTWARE", "image_url": "https://example.com/streaming.jpg", "home_url": "https://example.com/home" }'
    response = requests.post('https://api-m.sandbox.paypal.com/v1/catalogs/products', headers=headers, data=data)


def create_plan(headers):
    # Template
    data = '{ "product_id": "PROD-126180201M064221R", "name": "Basic", "description": "Basic", "status": "ACTIVE", "billing_cycles": [ { "frequency": { "interval_unit": "MONTH", "interval_count": 1 }, "tenure_type": "TRIAL", "sequence": 1, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "3", "currency_code": "USD" } } }, { "frequency": { "interval_unit": "MONTH", "interval_count": 1 }, "tenure_type": "TRIAL", "sequence": 2, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "6", "currency_code": "USD" } } }, { "frequency": { "interval_unit": "MONTH", "interval_count": 1 }, "tenure_type": "REGULAR", "sequence": 3, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "10", "currency_code": "USD" } } } ], "payment_preferences": { "auto_bill_outstanding": true, "setup_fee": { "value": "10", "currency_code": "USD" }, "setup_fee_failure_action": "CONTINUE", "payment_failure_threshold": 3 }, "taxes": { "percentage": "10", "inclusive": false } }'
    # Yearly
    data = '{ "product_id": "PROD-126180201M064221R", "name": "Yearly", "description": "Yearly", "status": "ACTIVE", "billing_cycles": [ { "frequency": { "interval_unit": "YEAR", "interval_count": 1 }, "tenure_type": "REGULAR", "sequence": 1, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "1200", "currency_code": "USD" } } } ], "payment_preferences": { "auto_bill_outstanding": true,  "setup_fee_failure_action": "CONTINUE", "payment_failure_threshold": 3 },  }'
    # Semi-Annual
    data = '{ "product_id": "PROD-126180201M064221R", "name": "Semi-Annual", "description": "Semi_Annual", "status": "ACTIVE", "billing_cycles": [ { "frequency": { "interval_unit": "MONTH", "interval_count": 6 }, "tenure_type": "REGULAR", "sequence": 1, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "750", "currency_code": "USD" } } } ], "payment_preferences": { "auto_bill_outstanding": true,  "setup_fee_failure_action": "CONTINUE", "payment_failure_threshold": 3 } }'
    # Monthly
    data = '{ "product_id": "PROD-126180201M064221R", "name": "Monthly", "description": "Monthly", "status": "ACTIVE", "billing_cycles": [ { "frequency": { "interval_unit": "MONTH", "interval_count": 1 }, "tenure_type": "REGULAR", "sequence": 1, "total_cycles": 0, "pricing_scheme": { "fixed_price": { "value": "150", "currency_code": "USD" } } } ], "payment_preferences": { "auto_bill_outstanding": true,  "setup_fee_failure_action": "CONTINUE", "payment_failure_threshold": 3 },  }'
    data_dict = json.loads(data)
    response = requests.post('https://api-m.sandbox.paypal.com/v1/billing/plans', headers=headers, data=data)
    return response
