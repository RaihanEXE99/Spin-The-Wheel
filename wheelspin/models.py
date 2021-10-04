from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime
from dateutil.parser import parse
import maya
import uuid
from .utils import generate_ref_code

# Create your models here.
class Credits(models.Model):
    user_f = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    def __str__(self):
        return str(self.user_f)
    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'Credits'

class Rooms(models.Model):
    room_name = models.CharField(max_length=100)
    users_m = models.ManyToManyField(User, related_name="user_m")
    bet = models.IntegerField()
    total = models.IntegerField()
    deg = models.IntegerField()
    showed = models.ManyToManyField(User, related_name="showed",blank=True)
    winner = models.CharField(max_length=100,default="NO WINNER")
    status = models.CharField(max_length=20,default="RUNNING")
    def __str__(self):
        return str(self.room_name)
    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'Rooms'


class GameDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.BigIntegerField()
    capcity = models.BigIntegerField()
    result = models.CharField(max_length=10)
    charge = models.FloatField()
    
    time = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __str__(self):
        date_time_str = str(self.time)
        date_time_obj = maya.parse(date_time_str).datetime()
        return (self.username.username + " " + str(date_time_obj.date()) + " " + str(date_time_obj.time().strftime("%I:%M %p")) + " " + str(date_time_obj.tzinfo))
    


class BalanceDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    transactionType = models.CharField(max_length=20)
    balance = models.FloatField()
    charge = models.FloatField()
    time = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        date_time_str = str(self.time)
        date_time_obj = maya.parse(date_time_str).datetime()
        return (self.username + " " + str(date_time_obj.date()) + " " + str(date_time_obj.time().strftime("%I:%M %p")) + " " + str(date_time_obj.tzinfo))


class Slots(models.Model):
    capacity = models.IntegerField()
    bet = models.IntegerField()
    charge = models.IntegerField(default=10)
    def __str__(self):
        return str("BET:" + str(self.bet) + "->" + "Capacity:"+ str(self.capacity))
    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'Slots'


class RefferUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=12, blank=True)
    ref_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="ref_by")

    def __str__(self):
        return f"{self.user.username} - {self.code}"

    def get_recommend_profiles(self):
        pass

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code

        super().save(*args, **kwargs)

class RefBonus(models.Model):
    percent = models.FloatField()

class RefBonusDetails(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    bonus = models.FloatField()
    time = time = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        date_time_str = str(self.time)
        date_time_obj = maya.parse(date_time_str).datetime()
        # return (self.to_user + " " + str(date_time_obj.date()) + " " + str(date_time_obj.time().strftime("%I:%M %p")) + " " + str(date_time_obj.tzinfo))
        return (str(self.to_user) + " " + str(date_time_obj.date()) + " " + str(date_time_obj.time().strftime("%I:%M %p")) + " " + str(date_time_obj.tzinfo))