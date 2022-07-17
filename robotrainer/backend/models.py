from django.db import models

class RobotInfo(models.Model):
    robotID = models.IntegerField(primary_key=True);
    speed = models.IntegerField(blank=True, null=True);
    heading = models.IntegerField(blank=True, null=True);
    duration = models.FloatField(blank=True, null=True);
    angle = models.IntegerField(blank=True, null=True);
    left_motor = models.IntegerField(blank=True, null=True);
    right_motor = models.IntegerField(blank=True, null=True);
    reward_data = models.IntegerField(blank=True, null=True);
    action_data = models.CharField(max_length=255);
    stabilization = models.SmallIntegerField(blank=True, null=True);  


class RobotAvailability(models.Model):
    robotId = models.OneToOneField(RobotInfo, primary_key=True, on_delete=models.CASCADE);
    availabile = models.SmallIntegerField(blank=True, null=True); 
