# Generated by Django 3.2.9 on 2022-07-18 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_delete_customjsonform'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomJsonForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_input_data', models.TextField(default='{}')),
            ],
        ),
    ]
