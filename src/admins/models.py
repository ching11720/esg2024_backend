# from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import RegexValidator

# class Employee(models.Model):
#     EID = models.CharField(max_length=12, primary_key=True)
#     name = models.CharField(max_length=255)
#     gender = models.IntegerField()
#     email = models.EmailField()
#     phone = models.CharField(max_length=11)
#     nation = models.CharField(max_length=255)
#     status = models.IntegerField(default=1)

#     def __str__(self):
#         return self.name
    
#     class Mata:
#         managed = False
#         db_table = 'employees'
# """
# class Project(models.Model):
#     pid_validator = RegexValidator(regex=r'^01[0-9]{6}$', message="PID must be in the format '01' followed by 6 digits.")

#     PID = models.CharField(max_length=10, primary_key=True, validators=[pid_validator])
#     pname = models.CharField(max_length=255)
#     flow = models.TextField(null=True, blank=True)
#     PMID = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='EID')
#     # PMID = models.CharField(max_length=10)
#     def __str__(self):
#         return self.pname

#     class Mata:
#         managed = False
#         db_table = 'projects'

# class WorksOn(models.Model):
#     EID = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='EID')
#     PID = models.ForeignKey(Project, on_delete=models.CASCADE, db_column='PID')
#     position = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'works_on'
#         unique_together = (('EID', 'PID'),)
#         indexes = [
#             models.Index(fields=['PID'], name='PID_idx'),
#         ]

#     def __str__(self):
#         return f"{self.EID} works on {self.PID} as {self.position}"
    
# class Usage(models.Model):
#     PID = PID = models.ForeignKey(Project, on_delete=models.CASCADE, db_column='PID')
#     EQID = models.CharField(max_length=12)
#     MID = models.CharField(max_length=14)

#     def __str__(self):
#         return f"{self.PID} uses {self.EQID}{self.MID}"


# """