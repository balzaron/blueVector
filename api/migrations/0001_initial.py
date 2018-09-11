# Generated by Django 2.1.1 on 2018-09-11 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(auto_created=True, default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('college', models.CharField(blank=True, default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=11, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('tags1', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ('created_time',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(auto_created=True, default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=10)),
                ('age', models.IntegerField(default=18)),
                ('identification', models.CharField(blank=True, max_length=18)),
                ('record', models.CharField(choices=[('高中', '高中'), ('小学', '小学'), ('初中', '初中'), ('大专', '大专'), ('中专', '中专')], max_length=100)),
                ('targetCollege', models.CharField(blank=True, choices=[('dalian', '大连理工大学'), ('dongbei', '东北大学'), ('kuangda', '中国矿业大学'), ('changsha', '长沙医学院'), ('hunan', '湖南医药学院')], max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('professional', models.CharField(max_length=100)),
                ('note', models.TextField()),
            ],
            options={
                'ordering': ('created_time',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(auto_created=True, default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('describe', models.CharField(default='', max_length=500)),
                ('recommend', models.CharField(default='***', max_length=5)),
                ('bReward', models.BooleanField(default=False)),
                ('reward', models.IntegerField(default=200)),
            ],
            options={
                'ordering': ('created_time',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(auto_created=True, default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('msg1', models.CharField(max_length=210)),
                ('msg2', models.CharField(max_length=210)),
                ('msg3', models.CharField(max_length=210)),
                ('release_time', models.CharField(max_length=250)),
                ('skill', models.CharField(max_length=255)),
                ('responsibilities', models.CharField(max_length=255)),
                ('introduce', models.TextField()),
                ('address', models.TextField()),
                ('tags', models.TextField()),
            ],
            options={
                'ordering': ('created_time',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(auto_created=True, default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('href', models.URLField(default='http://www.lanxiangren.net')),
                ('img', models.URLField(default=None)),
                ('title', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('msg1', models.CharField(max_length=210)),
                ('msg2', models.CharField(max_length=210)),
                ('msg3', models.CharField(max_length=210)),
                ('label', models.CharField(max_length=200)),
                ('tags1', models.CharField(max_length=255)),
                ('tags2', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('created_time',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LifeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(auto_created=True, default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('job_id', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=200)),
                ('in_time', models.CharField(blank=True, max_length=255)),
                ('out_time', models.CharField(blank=True, max_length=255)),
                ('company_phone', models.CharField(blank=True, max_length=11, null=True)),
                ('agent_phone', models.CharField(blank=True, max_length=11, null=True)),
                ('sign_num', models.IntegerField(blank=True, null=True)),
                ('tags1', models.CharField(blank=True, max_length=255)),
                ('tags2', models.CharField(blank=True, max_length=255)),
                ('tags3', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ('created_time',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(auto_created=True, default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=11)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=6)),
                ('identification', models.CharField(default='', max_length=18)),
                ('age', models.IntegerField(default=20)),
                ('location', models.TextField(default='', max_length=255)),
                ('describe', models.CharField(default='', max_length=500)),
                ('agent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Agent')),
            ],
            options={
                'ordering': ('created_time',),
            },
        ),
    ]