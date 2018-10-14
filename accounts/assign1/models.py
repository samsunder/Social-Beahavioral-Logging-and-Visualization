from django.db import models

# Create your models here.


class UserData(models.Model):
    username = models.CharField(max_length=20, unique=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=20, default="")

class Queries(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)
    text = models.CharField(max_length=10000)
    code = models.CharField(max_length=1000)
    user_id = models.IntegerField()
    time = models.IntegerField()
    vote = models.IntegerField()
    reputation = models.IntegerField()
    tag = models.CharField(max_length=1000)

class Solutions(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)
    text = models.CharField(max_length=10000)
    code = models.CharField(max_length=1000)
    user_id = models.IntegerField()
    time = models.IntegerField()
    vote = models.IntegerField()
    reputation = models.IntegerField()
    tag = models.CharField(max_length=1000)
    accepted_ans = models.IntegerField()
    q_id =models.ForeignKey(Queries,on_delete=models.CASCADE)



class EventsLog(models.Model):
    userid=models.ForeignKey(UserData,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    event=models.CharField(max_length=30)
    currentTime=models.DateTimeField(null=True)

class TimeLog(models.Model):
    time1 = models.DateTimeField()
    time2 = models.DateTimeField()
    time3 = models.DateTimeField()

