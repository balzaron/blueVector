from .models import *
from rest_framework import serializers

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
        fields = ('id','name', 'college', 'phone', 'password')


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('href', 'img', 'title', 'salary', 'name', 'msg1', 'msg2', 'msg3', 'label')


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetail
        fields = '__all__'


class LifeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeLog
        fields = '__all__'