from django.db import models

# Create your models here.
class Device(models.Model):
    mfModel = models.CharField(max_length=32)       # Model name
    sfdi = models.CharField(max_length=32)          # Short-form device ID of the IEEE 2030.5 device. "097935300833"
    batteryStatus = models.IntegerField(default=1)  # Battery status
    ess_Qe = models.FloatField(default=0.0)         # ESS Qe (=Reactive Power)
    passedTime = models.IntegerField(default=0)     # Time after starting monitoring (5, 10, 15 ...)
    currentPowerSource = models.IntegerField()      # Current power source (1: Wind turbine / 2: Photovoltaic)
    command = models.IntegerField(default=0)        # Currently, command will be same with batteryStatus

    def __str__(self):
        return self.mfModel
