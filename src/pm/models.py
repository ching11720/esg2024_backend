from django.db import models
from django.contrib.auth.models import User

class Boundary(models.Model):
    BID = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    created_by = models.ForeignKey('Employee', related_name='created_boundaries', on_delete=models.CASCADE, to_field='EID', db_column='created_by')
    created_date = models.DateField()
    modified_by = models.ForeignKey('Employee', related_name='modified_boundaries', on_delete=models.CASCADE, to_field='EID', db_column='modified_by')
    modified_date = models.DateField()

    class Meta:
        db_table = 'boundary'
        constraints = [
            models.CheckConstraint(
                check=models.Q(BID__regex=r'^04[0-9]{9}$'),
                name='check_bid_format'
            ),
        ]

class DailyRecord(models.Model):
    dailyID = models.AutoField(primary_key=True)
    PID = models.ForeignKey('Project', on_delete=models.CASCADE, to_field='PID', db_column='PID')
    PN = models.ForeignKey('PPN', on_delete=models.CASCADE, to_field='PN', db_column='PN')
    date = models.DateField()
    runtime = models.FloatField(null=True, blank=True)
    amount = models.FloatField()
    unit = models.CharField(max_length=10)
    created_by = models.ForeignKey('Employee', related_name='created_DailyRecord', on_delete=models.CASCADE, to_field='EID', db_column='created_by')
    created_date = models.DateField()
    last_modified_by = models.ForeignKey('Employee', related_name='modified_DailyRecord', on_delete=models.CASCADE, to_field='EID', db_column='last_modified_by')
    last_modified_date = models.DateField()

    class Meta:
        db_table = 'daily_record'
        unique_together = (('PID', 'PN', 'date'),)

class DailyRecordModified(models.Model):
    dailyID_modified = models.AutoField(primary_key=True)
    dailyID_origin = models.ForeignKey('DailyRecord', on_delete=models.CASCADE, to_field='dailyID', db_column='dailyID_origin')
    PID = models.ForeignKey('Project', on_delete=models.CASCADE, to_field='PID', db_column='PID')
    PN = models.ForeignKey('PPN', on_delete=models.CASCADE, to_field='PN', db_column='PN')
    date = models.DateField()
    runtime = models.FloatField(null=True, blank=True)
    amount = models.FloatField()
    unit = models.CharField(max_length=10)
    created_by = models.ForeignKey('Employee', on_delete=models.CASCADE, to_field='EID', db_column='created_by')
    created_date = models.DateField()
    status = models.IntegerField()

    class Meta:
        db_table = 'daily_record_modified'

class Emission(models.Model):
    emissionID = models.AutoField(primary_key=True)
    RID = models.ForeignKey('Resource', on_delete=models.CASCADE, to_field='RID', db_column='RID')
    GID = models.ForeignKey('GreenHouseGas', on_delete=models.CASCADE, to_field='GID', db_column='GID')
    amount_kg = models.FloatField()

    class Meta:
        db_table = 'emission'
        unique_together = (('RID', 'GID'),)

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

class GreenHouseGas(models.Model):
    GID = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    gwp = models.FloatField()

    class Meta:
        db_table = 'green_house_gas'

class PPN(models.Model):
    PN = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=255)
    total_amount = models.IntegerField()
    unit = models.CharField(max_length=20)

    class Meta:
        db_table = 'product_part_number'
        constraints = [
            models.CheckConstraint(
                check=models.Q(PN__regex=r'^06[0-9]{4}$'),
                name='check_pn_format'
            ),
        ]

class Project(models.Model):
    PID = models.CharField(max_length=10, primary_key=True)
    pname = models.CharField(max_length=255)
    flow = models.TextField(blank=True, null=True)
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

class RepairLog(models.Model):
    repairID = models.AutoField(primary_key=True)
    RID = models.ForeignKey('Resource', on_delete=models.CASCADE, to_field='RID', db_column='RID')
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'repair_log'

class Resource(models.Model):
    RID = models.CharField(max_length=14, primary_key=True)
    name = models.CharField(max_length=255)
    PN = models.ForeignKey('PPN', on_delete=models.CASCADE, to_field='PN', db_column='PN')
    amount = models.IntegerField()
    unit = models.CharField(max_length=10)
    purchase_date = models.DateField()
    disposal_date = models.DateField()
    age = models.IntegerField()
    SID = models.ForeignKey('Supplier', on_delete=models.CASCADE, to_field='SID', db_column='SID')
    factor = models.FloatField(null=True, blank=True, default=0)
    form = models.CharField(max_length=10, null=True, blank=True)
    category = models.CharField(max_length=10, null=True, blank=True)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'resource'
        constraints = [
            models.CheckConstraint(
                check=models.Q(RID__regex=r'^03[0-9]{12}$'),
                name='check_rid_format'
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

class Usage(models.Model):
    usageID = models.AutoField(primary_key=True)
    PID = models.ForeignKey('Project', on_delete=models.CASCADE, to_field='PID', db_column='PID')
    PN = models.ForeignKey('PPN', on_delete=models.CASCADE, to_field='PN', db_column='PN')
    amount = models.IntegerField()
    unit = models.CharField(max_length=45)

    class Meta:
        db_table = 'usage'
        unique_together = (('PID', 'PN'),)

class WorksOn(models.Model):
    workID = models.AutoField(primary_key=True)
    EID = models.ForeignKey('Employee', to_field='EID', on_delete=models.CASCADE, db_column='EID')
    PID = models.ForeignKey('Project', to_field='PID', on_delete=models.CASCADE, db_column='PID')
    position = models.CharField(max_length=255)
    role_on_sys = models.CharField(max_length=100)

    class Meta:
        db_table = 'works_on'
        unique_together = (('EID', 'PID'),)
