from django.db import models
from django import forms 

forms=(
    (1,1),
    (2,2),
    (3,3),
    (4,4)
)
streams=(
    ('G','G'),
    ('B','B'),
    ('H','H'),
    ('S','S'),
    ('F','F'),
    ('A','A')
)

subjects_on_offer=(
    ('MATH','MATH'),
    ('ENG','ENG')
)

class StudentDetail(models.Model):
    First_name=models.CharField(max_length=255)
    Middle_name=models.CharField(max_length=255,default=None)
    Last_name=models.CharField(max_length=255,default=None)
    
    adm_no=models.IntegerField()
    Form=models.IntegerField(choices=forms)
    Stream=models.CharField(max_length=1,choices=streams)
    #subjects=models.CharField(max_length=5,choices=subjects_on_offer)
    
    

    def __str__(self):
        return self.First_name.title()+' '+self.Middle_name.title()+' '+self.Last_name.title()

    def get_absolute_url(self):
        return reverse("StudentDetail_detail", kwargs={"pk": self.pk})
