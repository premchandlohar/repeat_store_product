# Generated by Django 3.0.6 on 2020-06-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=30)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('branch', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
            ],
        ),
    ]
