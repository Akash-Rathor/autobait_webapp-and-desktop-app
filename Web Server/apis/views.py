# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.renderers import JSONRenderer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
import requests,pickle
from django.shortcuts import render, redirect
from core.models import(
    linkedincredentials as lc
)
# Create your views here.


@api_view(['GET'])
def GetLinkedinCredentials(request):
    '''
    headers = {'Authorization':'Token tokenid',}
    response = requests.get('http://127.0.0.1:8000/api/verifyprofile/',headers=headers)
    '''
    username,password = lc.objects.values_list('username','password').get(user_id=request.user.id)
    context = {
        'user':username,
        'auth':pickle.loads(password),
    }
    return Response(context)