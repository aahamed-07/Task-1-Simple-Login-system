# Generated by Django 4.0.2 on 2022-04-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_alter_doc_table_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='patient_table',
        ),
        migrations.AlterField(
            model_name='doc_table',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]