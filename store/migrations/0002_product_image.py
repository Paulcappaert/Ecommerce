# Generated by Django 2.0.10 on 2019-04-01 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
