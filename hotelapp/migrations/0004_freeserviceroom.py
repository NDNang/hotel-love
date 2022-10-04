# Generated by Django 3.2.7 on 2022-10-03 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0003_priceroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeServiceRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.room')),
            ],
            options={
                'db_table': 'free_services',
            },
        ),
    ]