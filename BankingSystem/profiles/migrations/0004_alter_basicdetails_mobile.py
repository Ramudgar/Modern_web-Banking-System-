# Generated by Django 3.2.7 on 2021-09-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_enter_the_amount_to_be_transferred_in_inr_moneytransfer_enter_the_amount_to_be_transferred_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='mobile',
            field=models.CharField(default=0, max_length=15),
        ),
    ]