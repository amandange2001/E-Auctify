# Generated by Django 5.0.1 on 2024-02-19 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_auctionapp', '0005_alter_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=20),
        ),
    ]
