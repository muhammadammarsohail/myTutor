# Generated by Django 3.2.4 on 2021-06-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
