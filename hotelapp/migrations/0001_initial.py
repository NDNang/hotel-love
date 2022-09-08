# Generated by Django 3.2.7 on 2022-09-08 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('fullname', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('sum_success', models.IntegerField(blank=True, default=0, null=True)),
                ('sum_fail', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='ExtraService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'extra_service',
            },
        ),
        migrations.CreateModel(
            name='ListCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'list_code',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=500)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('images', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'db_table': 'list_room',
            },
        ),
        migrations.CreateModel(
            name='ImageRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=50)),
                ('images', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.room')),
            ],
            options={
                'db_table': 'image_room',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('percent', models.IntegerField(blank=True, null=True)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.room')),
            ],
            options={
                'db_table': 'discount_room',
            },
        ),
        migrations.CreateModel(
            name='BookRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('date_in', models.DateTimeField()),
                ('date_out', models.DateTimeField()),
                ('is_pay', models.BooleanField(default=False)),
                ('total', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('code_pay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.listcode')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.customer')),
                ('extra_service', models.ManyToManyField(blank=True, related_name='book_room', to='hotelapp.ExtraService')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.room')),
            ],
            options={
                'db_table': 'book_room',
            },
        ),
    ]
