# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-10 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='privacy_controls',
        ),
        migrations.AddField(
            model_name='product',
            name='customer_support_easy',
            field=models.NullBooleanField(help_text='Makes it easy to contact customer support?'),
        ),
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.CharField(blank='True', help_text='Email', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='live_chat',
            field=models.CharField(blank='True', help_text='Live Chat', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='manage_security',
            field=models.NullBooleanField(help_text='Manages security vulnerabilities?'),
        ),
        migrations.AddField(
            model_name='product',
            name='must_change_default_password',
            field=models.NullBooleanField(help_text='Must change a default password?'),
        ),
        migrations.AddField(
            model_name='product',
            name='phone_number',
            field=models.CharField(blank='True', help_text='Phone Number', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates',
            field=models.NullBooleanField(help_text='Security updates?'),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption',
            field=models.NullBooleanField(help_text='Does the product use encryption?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank='True', help_text='Price', max_length=100),
        ),
    ]