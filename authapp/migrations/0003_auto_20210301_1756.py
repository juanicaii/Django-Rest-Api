# Generated by Django 3.1.7 on 2021-03-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210227_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
