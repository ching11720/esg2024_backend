from django.db import models
from django.core.validators import RegexValidator

class Boundary(models.Model):
    bid_validator = RegexValidator(regex=r'^05[0-9]{9}$', message="PID must be in the format '01' followed by 6 digits.")

    BID = models.CharField(max_length=11, primary_key=True, validators=[bid_validator])
    bname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.bname
    """
    class Meta:
        managed = False
        db_table = 'boundarys'
    """

class Source(models.Model):
    sid_validator = RegexValidator(regex=r'^06[0-9]{10}$', message="PID must be in the format '01' followed by 6 digits.")

    SID = models.CharField(max_length=12, primary_key=True, validators=[sid_validator])
    ename = models.CharField(max_length=255)
    form = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    category = models.IntegerField()

    def __str__(self):
        return self.sname
    """
    class Meta:
        managed = False
        db_table = 'boundarys'
    """
