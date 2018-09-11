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
            name='Course',
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
            name='CourseDetail',
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
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(auto_created=True, default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('describe', models.CharField(blank=True, default='', max_length=500)),
                ('recommend', models.CharField(blank=True, default='***', max_length=5)),
                ('bReward', models.BooleanField(blank=True, default=False)),
                ('reward', models.IntegerField(blank=True, default=200)),
                ('tags', models.CharField(blank=True, max_length=255)),
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
                ('identification', models.CharField(blank=True, default='', max_length=18)),
                ('age', models.IntegerField(blank=True, default=20)),
                ('location', models.TextField(blank=True, default='', max_length=255)),
                ('describe', models.CharField(blank=True, default='', max_length=500)),
                ('agent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='trainning.Agent')),
            ],
            options={
                'ordering': ('created_time',),
            },
        ),
    ]
