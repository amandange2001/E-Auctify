# Generated by Django 5.0.1 on 2024-02-18 19:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_auctionapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingProduct',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='e_auctionapp.product')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(default='Upcoming', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Antiques', 'Antiques'), ('Electronics', 'Electronics'), ('Furnitures', 'Furnitures'), ('Paintings', 'Paintings')], default='', max_length=50),
        ),
        migrations.CreateModel(
            name='ClosedProduct',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='e_auctionapp.product')),
                ('closing_time', models.DateTimeField()),
                ('final_price', models.FloatField()),
                ('is_sold', models.BooleanField(default=False)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]