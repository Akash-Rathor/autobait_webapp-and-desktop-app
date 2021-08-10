
# core/views.py
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from social_django.models import UserSocialAuth as social_user
import requests
import pickle
from .models import (
  linkedincredentials,
)
from rest_framework.authtoken.models import Token

# class TokenViewSet(viewsets.ModelViewSet):
#   renderer_classes = [JSONRenderer]
#   queryset = Token.objects.all()
#   serializer_class = Tokenserializers
#   lookup_field = 'key'

def login(request):
  if User.is_authenticated and User.is_anonymous==True:
    return redirect('home')
  return render(request, 'home/home.html')

'''
Below function checks if user is superuser, if its annonymous user or if it is authenticated or not.
and also it extract profile picture from via making call to linkedin server by extracting access token from extradata column 
of database
'''
@login_required
def home(request):
  if request.user.is_authenticated and request.user.is_superuser==False or User.is_anonymous==False and request.user.is_superuser==False:
    if not Token.objects.filter(user_id = request.user.id).exists():
      token = Token.objects.create(user_id=request.user.id)
      print(request.POST)
    return render(request, 'dashboard/index.html')
  else:
    return render(request, 'home/home.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
    

@login_required
def settings(request):
  context = {
    'user_data':User.objects.get(id =request.user.id),
    'token_id':Token.objects.get(user_id=request.user.id).key
  }
  if linkedincredentials.objects.filter(user_id=request.user).exists():
    context['exists'] = True
    val = linkedincredentials.objects.get(user_id=request.user)
    context['linkedindata_username'] = val.username
    context['linkedindata_password'] = pickle.loads(val.password)
  else:
    context['exists'] = False

  if request.method=='POST':
    username = request.POST['username']
    password = pickle.dumps(request.POST['password'])
    if linkedincredentials.objects.filter(user_id=request.user).exists():
        val = linkedincredentials.objects.get(user_id=request.user)
        val.password = password
        val.username = username
        val.save()
        context['exists'] = True
        context['linkedindata_username'] = val.username
        context['linkedindata_password'] = pickle.loads(val.password)
    else:
      linkedincredentials(user_id = request.user,username = username,password = password).save()
      val = linkedincredentials.objects.get(user_id=request.user)
      context['exists'] = True
      context['linkedindata_username'] = val.username
      context['linkedindata_password'] = pickle.loads(val.password)
    return render(request,'settings/index.html',{'context':context})
  return render(request,'settings/index.html',{'context':context})

@login_required
def campaigns(request,val):
  template = f'{val}.html'

  if request.method=="POST":
    print(request.POST)
    if 'campaignmode' in request.POST:
        request.session['campaignmode'] = request.POST['campaignmode']

    if 'urlinputtype' in request.POST:
        request.session['urlinputtype'] = request.POST['urlinputtype']

    if 'searchedurl' in request.POST:
      request.session['searchedurl']=request.POST['searchedurl']
      request.session['leads']=request.POST['leads']

    return redirect(campaigns,val=val)

  return render(request,f'campaigns/{template}')



def finaldatashowpage(request):
  if request.method=='POST':
    print(request.POST)
    return redirect('finaldatashowpage')
  return render(request,'campaigns/5.html')