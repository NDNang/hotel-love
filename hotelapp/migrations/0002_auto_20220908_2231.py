# Generated by Django 3.2.7 on 2022-09-08 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookroom',
            old_name='code_pay',
            new_name='code',
        ),
        migrations.AlterField(
            model_name='discount',
            name='percent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True),
        ),
    ]
