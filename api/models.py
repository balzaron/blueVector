from django.db import models
from .enums import *
# Create your models here.


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False, auto_created=True)

    class Meta:
        ordering = ('created_time', )
        abstract = True


class User(BaseModel):

    name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=11, default='')
    sex = models.CharField(max_length=6, choices=sexes)
    identification = models.CharField(max_length=18, default='')
    age = models.IntegerField(default=20)
    location = models.TextField(max_length=255, default='')
    describe = models.CharField(max_length=500, default='')
    agent = models.ForeignKey('Agent', to_field='id', default=None, on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ('created_time',)


class Institution(BaseModel):

    name = models.CharField(max_length=100, default='')
    describe = models.CharField(max_length=500, default='')
    recommend = models.CharField(max_length=5, default='***')
    bReward = models.BooleanField(default=False)
    reward = models.IntegerField(default=200)


class Agent(BaseModel):

    name = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=11, default='',unique=True)
    password = models.CharField(max_length=255)
    tags1 = models.CharField(max_length=255, blank=True)


class Education(BaseModel):

    name = models.CharField(max_length=100, default='')
    sex = models.CharField(max_length=10, choices=sexes)
    age = models.IntegerField(default=18)
    identification = models.CharField(max_length=18, blank=True)
    record = models.CharField(max_length=100, choices=edu)
    targetCollege = models.CharField(max_length=100, choices=universities, blank=True)
    phone = models.CharField(max_length=11)
    professional = models.CharField(max_length=100)
    note = models.TextField()


class Jobs(BaseModel):

    href = models.URLField(default="http://www.lanxiangren.net")
    img = models.URLField(default=None)
    title = models.CharField(max_length=255)
    salary = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    msg1 = models.CharField(max_length=210)
    msg2 = models.CharField(max_length=210)
    msg3 = models.CharField(max_length=210)
    label = models.CharField(max_length=200)
    tags1 = models.CharField(max_length=255)
    tags2 = models.CharField(max_length=255)


class JobDetail(BaseModel):

    title = models.CharField(max_length=255)
    salary = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    msg1 = models.CharField(max_length=210)
    msg2 = models.CharField(max_length=210)
    msg3 = models.CharField(max_length=210)
    release_time = models.CharField(max_length=250)
    skill = models.CharField(max_length=255)
    responsibilities = models.CharField(max_length=255)
    introduce = models.TextField()
    address = models.TextField()
    tags = models.TextField()


class LifeLog(BaseModel):

    phone = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100, blank=True)
    job_id = models.IntegerField()
    status = models.CharField(max_length=200, blank=True)
    in_time = models.CharField(max_length=255, blank=True)
    out_time = models.CharField(max_length=255, blank=True)
    company_phone = models.CharField(max_length=11, blank=True, null=True)
    agent_phone = models.CharField(max_length=11, blank=True, null=True)
    sign_num = models.IntegerField(blank=True, null=True)
    tags1 = models.CharField(max_length=255, blank=True)
    tags2 = models.CharField(max_length=255, blank=True)
    tags3 = models.CharField(max_length=255, blank=True)
