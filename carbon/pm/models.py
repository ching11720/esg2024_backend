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
    PMID = models.ForeignKey('User', on_delete=models.CASCADE)

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
    SID = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    EQID = models.ForeignKey('Equipment', null=True, blank=True, on_delete=models.SET_NULL)
    MID = models.ForeignKey('Material', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'supply'

class Usage(models.Model):
    PID = models.ForeignKey('Project', on_delete=models.CASCADE)
    EQID = models.ForeignKey('Equipment', null=True, blank=True, on_delete=models.SET_NULL)
    MID = models.ForeignKey('Material', null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    unit = models.CharField(max_length=45)

    class Meta:
        db_table = 'usage'

class User(models.Model):
    UID = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=255)
    access = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'

class WorksOn(models.Model):
    EID = models.ForeignKey('Employee', on_delete=models.CASCADE)
    PID = models.ForeignKey('Project', on_delete=models.CASCADE)
    position = models.CharField(max_length=255)

    class Meta:
        db_table = 'works_on'
        unique_together = (('EID', 'PID'),)
