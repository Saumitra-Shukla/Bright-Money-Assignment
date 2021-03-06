# Generated by Django 3.1.5 on 2021-01-13 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlaidApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=100)),
                ('balance_available', models.FloatField(default=None, null=True)),
                ('balance_current', models.FloatField()),
                ('currency', models.CharField(max_length=5)),
                ('limit', models.FloatField(default=None, null=True)),
                ('acc_type', models.CharField(max_length=100)),
                ('acc_name', models.CharField(max_length=100)),
                ('bank_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlaidApp.bankitemmodel')),
            ],
        ),
    ]
