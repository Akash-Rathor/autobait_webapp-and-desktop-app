from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class linkedincredentials(TimeStampMixin):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=200,unique=True)
    password = models.BinaryField(max_length=200)

#campaign database
class paidOrFree(TimeStampMixin):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    dayleft = models.BooleanField(default=False)#need to check and update everytime user login to see if user have free use days left  or not

class campaign(TimeStampMixin):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    campaignUrl = models.CharField(max_length=350)
    maximumLead = models.IntegerField()
    message = models.CharField(max_length=500)


class campaignFlow(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    campaignId = models.ForeignKey(campaign, on_delete=models.CASCADE)
    runWhen = models.DateTimeField()
    actionId = models.IntegerField()
    message = models.TextField(max_length=700)

class LeftUrl(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    lefturl = models.CharField(max_length=400)

class DoneUrl(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    image_url = models.CharField(max_length=400)
    
class CampaignUrls(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    campaignId =  models.ForeignKey(campaign, on_delete=models.CASCADE)
    # totalUrls = models.IntegerField()
    requestStatus = models.BooleanField(default=False)
    FollowStatus = models.BooleanField(default=False)
    connectionMessage = models.CharField(max_length=500)
    urlId = models.ForeignKey(LeftUrl, on_delete=models.CASCADE)
    followUpMessage= models.CharField(max_length=700)
    # imageUrl= models.CharField()
    # name = models.CharField(max_length=100)


class message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    urlId = models.ForeignKey(CampaignUrls, on_delete=models.CASCADE)
    leftUrl = models.CharField(max_length=200)


