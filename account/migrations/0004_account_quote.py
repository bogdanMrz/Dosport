# Generated by Django 3.1.7 on 2021-09-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='quote',
            field=models.CharField(blank=1, max_length=30, null=1),
            preserve_default=1,
        ),
    ]
