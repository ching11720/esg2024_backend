from django.db import models
from django.contrib.auth.models import User

class Boundary(models.Model):
    BID = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=100)

    class Meta:
        db_table = 'boundary'
        constraints = [
            models.CheckConstraint(
                check=models.Q(BID__regex=r'^04[0-9]{9}$'),
                name='check_bid_format'
            ),
        ]

class Emission(models.Model):
    SRID = models.ForeignKey('Source', on_delete=models.CASCADE, to_field='SRID', db_column='SRID')
    GID = models.ForeignKey('Gas', on_delete=models.CASCADE, to_field='GID', db_column='GID')
    amount = models.FloatField()

    class Meta:
        db_table = 'emission'
        unique_together = (('SRID', 'GID'),)

class Employee(models.Model):
    EID = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    nation = models.CharField(max_length=255)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'employees'
        constraints = [
            models.CheckConstraint(
                check=models.Q(EID__regex=r'^02[0-9]{10}$'),
                name='check_eid_format'
            ),
            models.CheckConstraint(
                check=models.Q(email__regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
                name='check_email_format'
            ),
            models.CheckConstraint(
                check=models.Q(phone__regex=r'^[0-9]+$'),
                name='check_phone_format'
            ),
            models.CheckConstraint(
                check=models.Q(gender__in=[1, 2]),
                name='employees_chk_1'
            ),
        ]

class Gas(models.Model):
    GID = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    gwp = models.FloatField()

    class Meta:
        db_table = 'gas'

class Project(models.Model):
    PID = models.CharField(max_length=10, primary_key=True)
    pname = models.CharField(max_length=255)
    flow = models.TextField(blank=True, null=True)
    # PMID = models.ForeignKey(User, on_delete=models.CASCADE, to_field='UID', db_column='PMID')
    PMID = models.ForeignKey('Employee', on_delete=models.CASCADE, to_field='EID', db_column='PMID')
    BID = models.ForeignKey('Boundary', on_delete=models.CASCADE, to_field='BID', db_column='BID')

    class Meta:
        db_table = 'projects'
        constraints = [
            models.CheckConstraint(
                check=models.Q(PID__regex=r'^01[0-9]{6}$'),
                name='check_pid_format'
            ),
        ]

class Record(models.Model):
    PID = models.ForeignKey('Project', on_delete=models.CASCADE, to_field='PID', db_column='PID')
    SRID = models.ForeignKey('Source', on_delete=models.CASCADE, to_field='SRID', db_column='SRID')
    date = models.DateField()
    runtime = models.FloatField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'record'
        unique_together = (('PID', 'SRID', 'date'),)

class Source(models.Model):
    SRID = models.CharField(max_length=14, primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    unit = models.CharField(max_length=10)
    purchase_date = models.DateField()
    disposal_date = models.DateField()
    age = models.IntegerField()
    factor = models.FloatField(null=True, blank=True)
    form = models.CharField(max_length=10, null=True, blank=True)
    category = models.CharField(max_length=10, null=True, blank=True)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'source'
        constraints = [
            models.CheckConstraint(
                check=models.Q(SRID__regex=r'^03[0-9]{12}$'),
                name='check_srid_format'
            ),
        ]

class Supplier(models.Model):
    SID = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    nation = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'suppliers'
        constraints = [
            models.CheckConstraint(
                check=models.Q(SID__regex=r'^05[0-9]{10}$'),
                name='check_sid_format'
            ),
            models.CheckConstraint(
                check=models.Q(phone__regex=r'^[0-9]+$'),
                name='check_sphone_format'
            ),
        ]

class Supply(models.Model):
    SID = models.ForeignKey('Supplier', on_delete=models.CASCADE, to_field='SID', db_column='SID')
    SRID = models.ForeignKey('Source', on_delete=models.CASCADE, to_field='SRID', db_column='SRID')

    class Meta:
        db_table = 'supply'
        unique_together = (('SID', 'SRID'),)

class Usage(models.Model):
    PID = models.ForeignKey('Project', on_delete=models.CASCADE, to_field='PID', db_column='PID')
    SRID = models.ForeignKey('Source', on_delete=models.CASCADE, to_field='SRID', db_column='SRID')
    amount = models.IntegerField()
    unit = models.CharField(max_length=45)

    class Meta:
        db_table = 'usage'
        unique_together = (('PID', 'SRID'),)

class User(models.Model):
    UID = models.OneToOneField('Employee', to_field='EID', on_delete=models.CASCADE, db_column='UID')
    password = models.CharField(max_length=255)
    access = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'

class WorksOn(models.Model):
    EID = models.ForeignKey('Employee', to_field='EID', on_delete=models.CASCADE, db_column='EID')
    PID = models.ForeignKey('Project', to_field='PID', on_delete=models.CASCADE, db_column='PID')
    position = models.CharField(max_length=255)

    class Meta:
        db_table = 'works_on'
        unique_together = (('EID', 'PID'),)
