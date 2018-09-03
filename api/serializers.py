from rest_framework import serializers
from .models import *


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'created', 'name', 'describe', 'price', 'isDelete')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'phone', 'sex', 'location','identification', 'age', 'describe', 'agent')


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'describe', 'bReward','recommend')


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('name', 'college', 'phone')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('name', 'sex', 'age', 'record', 'phone',
                  'professional', 'note')


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('href', 'img', 'title', 'salary', 'name', 'msg1', 'msg2', 'msg3',)


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetail
        fields = '__all__'


class LifeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeLog
        fields = '__all__'
