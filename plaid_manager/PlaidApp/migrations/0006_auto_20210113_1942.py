# Generated by Django 3.1.5 on 2021-01-13 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlaidApp', '0005_accountmodel_transactionmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountmodel',
            old_name='item',
            new_name='bank_item',
        ),
    ]
