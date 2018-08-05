from django.db import models

# Create your models here.


class User(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    bDeleted = models.BooleanField(default=False, auto_created=True)

    name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=11, default='')
    sex = models.CharField(max_length=6, choices=(('m','male'), ('f', 'female')))
    identification = models.CharField(max_length=18)
    age = models.IntegerField(default=20)
    location = models.TextField(max_length=255)
    describe = models.CharField(max_length=500, default='')
    agent = models.ForeignKey('Agent', to_field='id', default=None, on_delete=models.PROTECT)

    class Meta:
        ordering = ('created_time',)


class Institution(models.Model):
    #, auto_created=True, db_index=True, default=1
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    bDeleted = models.BooleanField(default=False, auto_created=True)

    name = models.CharField(max_length=100, default='')
    describe = models.CharField(max_length=500, default='')
    recommend = models.CharField(max_length=5, default='***')
    bReward = models.BooleanField(default=False)
    reward = models.IntegerField(default=200)
    class Meta:
        ordering = ('created_time',)


class Agent(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    bDeleted = models.BooleanField(default=False, auto_created=True)

    name = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=11, default='')

    class Meta:
        ordering = ('created_time', )
