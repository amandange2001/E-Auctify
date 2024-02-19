# Generated by Django 5.0.1 on 2024-02-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_auctionapp', '0007_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Upcoming', 'Upcoming'), ('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=20),
        ),
    ]
