# Generated by Django 4.2.3 on 2023-07-07 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mamamboga', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='mamamboga',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mamamboga.mamamboga'),
            preserve_default=False,
        ),
    ]