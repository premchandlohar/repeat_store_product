# Generated by Django 3.0.6 on 2020-05-19 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_userprofile_mobilenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='buildingname',
            new_name='building_name',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='streetname',
            new_name='street_name',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='userprofile',
            new_name='user_profile',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='createdon',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='mobilenumber',
            new_name='mobilen_umber',
        ),
    ]