# Generated by Django 4.2.1 on 2023-06-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accuracy',
            name='create',
            field=models.CharField(default='', max_length=100),
        ),
    ]
