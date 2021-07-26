from django.test import TestCase
import requests
# Create your tests here.


# to check user authentication status
def check_status(token):
    headers = {'Authorization':f'Token {token}',}
    response = requests.get('http://127.0.0.1:8000/api/verifyprofile/',headers=headers)
    if response.status_code==200:
        return 'User authenticated'# here we can return user credentials
    else:
        return 'User not authenticated'
