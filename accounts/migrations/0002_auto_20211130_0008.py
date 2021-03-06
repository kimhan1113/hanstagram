# Generated by Django 3.2.6 on 2021-11-29 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='24x24 이미지 사이즈', upload_to='accounts/avatar/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '남성'), ('F', '여성')], max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator('^$010-?[0-9]\\d{4}-?\\d{4}$')]),
        ),
    ]
