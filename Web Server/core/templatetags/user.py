from django import template
from django.contrib.auth.models import User
register = template.Library()
from social_django.models import UserSocialAuth as social_user
import requests

@register.simple_tag
def getuser_details(id):
    user=User.objects.get(id=id)
    Access_token = social_user.objects.get(user_id=user.id).extra_data['access_token']
    a = requests.get(f'https://api.linkedin.com/v2/me?projection=(id,profilePicture(displayImage~:playableStreams))&oauth2_access_token={Access_token}')
    image_url = a.json()['profilePicture']['displayImage~']['elements'][0]['identifiers'][0]['identifier']
    context1 ={
        'username':user.username,
        'first_name':user.first_name,
        'last_name':user.last_name,
        'email':user.last_name,
        'image_url':image_url,
    }
    return context1