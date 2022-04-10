# Generated by Django 4.0.2 on 2022-04-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doc_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=40)),
                ('confirm_password', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='patient_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=40)),
                ('confirm_password', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
