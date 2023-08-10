# Generated by Django 4.2.1 on 2023-06-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=16)),
                ('phonenumber', models.CharField(max_length=16)),
                ('location', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
