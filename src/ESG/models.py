# from django.db import models

# class Boundary(models.Model):
#     BID = models.CharField(max_length=11, primary_key=True)
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     type = models.CharField(max_length=255)
#     status = models.IntegerField(default=1)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         managed = False
#         db_table = 'boundarys'
    

# class Source(models.Model):
#     SID = models.CharField(max_length=12, primary_key=True)
#     Ename = models.CharField(max_length=255)
#     form = models.CharField(max_length=255)
#     MName = models.CharField(max_length=255)
#     category = models.IntegerField()
#     status = models.IntegerField(default=1)

#     def __str__(self):
#         return self.EName and self.MName
    
#     class Meta:
#         managed = False
#         db_table = 'sources'
    




# class Equipment(models.Model):
#     EQID = models.CharField(max_length=12, primary_key=True)
#     name = models.CharField(max_length=255)
#     amount = models.IntegerField()
#     unit = models.CharField(max_length=10)
#     coefficient = models.FloatField(null=True, blank=True)
#     purchase_date = models.DateField()
#     disposal_date = models.DateField()
#     age = models.IntegerField()
#     status = models.IntegerField(default=1)

#     class Meta:
#         db_table = 'equipments'

# class Material(models.Model):
#     MID = models.CharField(max_length=14, primary_key=True)
#     name = models.CharField(max_length=255)
#     amount = models.IntegerField()
#     unit = models.CharField(max_length=10)
#     coefficient = models.FloatField(null=True, blank=True)
#     purchase_date = models.DateField()
#     age = models.IntegerField()

#     class Meta:
#         db_table = 'materials'
