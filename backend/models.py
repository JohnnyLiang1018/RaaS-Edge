from statistics import mode
from django.db import models
from django import forms


class RobotInfo(models.Model):
    robotID = models.IntegerField(primary_key=True)
    speed = models.IntegerField(blank=True, null=True)
    heading = models.IntegerField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    angle = models.IntegerField(blank=True, null=True)
    left_motor = models.IntegerField(blank=True, null=True)
    right_motor = models.IntegerField(blank=True, null=True)
    reward_data = models.IntegerField(blank=True, null=True)
    action_data = models.CharField(max_length=255)
    stabilization = models.SmallIntegerField(blank=True, null=True)  


class RobotAvailability(models.Model):
    robotId = models.OneToOneField(RobotInfo, primary_key=True, on_delete=models.CASCADE)
    availabile = models.SmallIntegerField(blank=True, null=True) 

class InputForm(models.Model):
     number_of_robots = models.IntegerField(blank=True, null=True)
     number_of_loops = models.IntegerField(blank=True, null=True)
     list_of_commands = models.CharField(max_length=500)
    

     def __str__(self) -> str:
         return super().__str__()

class VectorForm(models.Model):
     vector_text_box = models.TextField(max_length=500)
     #vector_text_box = forms.CharField(widget=forms.Textarea)
    

     def __str__(self) -> str:
         return super().__str__()