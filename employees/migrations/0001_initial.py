# Generated by Django 4.2.11 on 2024-03-20 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='images/emp_photos/')),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]