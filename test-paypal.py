import os
import requests
from dotenv import load_dotenv

load_dotenv()
access_token = os.environ.get('PAYPAL_ACCESS_TOKEN')
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
def create_three_plans(headers):



