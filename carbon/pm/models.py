from django.db import models

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

class Equipment(models.Model):
    EQID = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    unit = models.CharField(max_length=10)
    coefficient = models.FloatField(null=True, blank=True)
    purchase_date = models.DateField()
    disposal_date = models.DateField()
    age = models.IntegerField()
    status = models.IntegerField(default=1)

    class Meta:
        db_table = 'equipments'

class Material(models.Model):
    MID = models.CharField(max_length=14, primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    unit = models.CharField(max_length=10)
    coefficient = models.FloatField(null=True, blank=True)
    purchase_date = models.DateField()
    age = models.IntegerField()

    class Meta:
        db_table = 'materials'

class Project(models.Model):
    PID = models.CharField(max_length=10, primary_key=True)
    pname = models.CharField(max_length=255)
    flow = models.TextField()
    PMID = models.ForeignKey('User', to_field='UID', on_delete=models.CASCADE, db_column='PMID')

    class Meta:
        db_table = 'projects'

class Supplier(models.Model):
    SID = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    nation = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'suppliers'

class Supply(models.Model):
    SID = models.ForeignKey('Supplier', to_field='SID', on_delete=models.CASCADE, db_column='SID')
    EQID = models.ForeignKey('Equipment', to_field='EQID', null=True, blank=True, on_delete=models.SET_NULL, db_column='EQID')
    MID = models.ForeignKey('Material', to_field='MID', null=True, blank=True, on_delete=models.SET_NULL, db_column='MID')

    class Meta:
        db_table = 'supply'

class UsageM(models.Model):
    PID = models.ForeignKey('Project', to_field='PID', on_delete=models.CASCADE, db_column='PID')
    MID = models.ForeignKey('Material', to_field='MID', on_delete=models.CASCADE, db_column='MID')
    amount = models.IntegerField(default=1)
    unit = models.CharField(max_length=45, default='unit')

    class Meta:
        db_table = 'usage_m'
        unique_together = ('PID', 'MID')

class UsageEq(models.Model):
    PID = models.ForeignKey('Project', to_field='PID', on_delete=models.CASCADE, db_column='PID')
    EQID = models.ForeignKey('Equipment', to_field='EQID', on_delete=models.CASCADE, db_column='EQID')
    amount = models.IntegerField(default=1)
    unit = models.CharField(max_length=45, default='unit')

    class Meta:
        db_table = 'usage_eq'
        unique_together = ('EQID', 'PID')

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
