from statistics import mode
from django.db import models
from django.forms import Form, JSONField
from django_jsonforms.forms import JSONSchemaField

input_schema = {
      "type": "object",
      "required": ["Name"],
      "properties": {
           "Name": {
                "type": "string",
                "maxLength": 30    
           },             
           "Speed": {
                "type": "integer",
                "maxLength": 30                 
           },
           "Heading": {
                "type": "integer",
                "maxLength": 30                 
           },
           "Duration": {
                "type": "integer",
                "maxLength": 30                 
           },
           "Angle": {
                "type": "integer",
                "maxLength": 30                 
           },
           "StateX": {
                "type": "integer",
                "maxLength": 30                 
           },
           "StateY": {
                "type": "integer",
                "maxLength": 30                 
           },
           "rewardData": {
                "type": "integer",
                "maxLength": 30                 
           },
           "ActionData": {
                "type": "string",
                "maxLength": 30                 
           },
           "Stabilization": {
                "type": "integer",
                "maxLength": 30                 
           }
        
      }    
    }

options = {"no_additional_properties": True,
            "theme": "bootstrap4"}


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

class CustomJsonForm(Form):
    customer_input_data = JSONSchemaField(schema = input_schema, options=options);
    # customer_input_data = models.TextField(default="{}");
    # customer_input_data = models.JSONField(null=True);