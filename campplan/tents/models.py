from copyreg import constructor
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Nation(models.Model):
    name = models.CharField(max_length=128, null=False, unique=True)
    player_nation = models.BooleanField()
    def __str__(self):
        return self.name

class FieldGroup(models.Model):
    name = models.CharField(max_length=128, null=False, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.name

class TentType(models.Model):
    name = models.CharField(max_length=128, null=False, unique=True)
    img = models.CharField(max_length=128, null=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=128, null=False, unique=True)
    date = models.DateField()
    def __str__(self):
        return self.name

class Tent(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=128, null=True)

    sleeping_only = models.BooleanField(default=False)
    group_tent = models.BooleanField(default=False)
    colour = models.CharField(max_length=64, null=True)
    occupants = models.IntegerField()
    pd_supplied = models.BooleanField(default=False)
    electric_req = models.BooleanField(default=False)
    notes = models.TextField()

    class TentOnField(models.TextChoices):
        IC_ESSENTIAL = "IC", _("IC Essential")
        NORMAL = "X", _("Normal")
        OOC_OKAY = "OC", _("OOC Okay")
    tent_on_field = models.CharField(max_length=2, choices=TentOnField.choices)

    class ETA(models.TextChoices):
        EARLY_CREW = "--", _("Before Thursday")
        THURSDAY_PM1 = "TA", _("Thursday before 3pm")
        THURSDAY_PM2 = "TB", _("Thursday before 3-6pm")
        THURSDAY_EVE = "TC", _("Thursday after 6pm")
        FRIDAY_AM = "FA", _("Friday before noon")
        FRIDAY_PM1 = "FB", _("Friday before 12-3pm")
        FRIDAY_PM2 = "FC", _("Friday after 3-5pm")
        FRIDAY_EVE = "FD", _("Friday after 5pm")

    def __str__(self):
        return self.owner if self.name is None else "%s : %s"%(self.owner, self.name)

class TentAtEvent(models.Model):
    tent = models.ForeignKey(Tent, on_delete=models.CASCADE, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["tent", "event"], name="tent_at_event_only_once")]