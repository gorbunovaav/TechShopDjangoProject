# Generated by Django 4.2.16 on 2024-11-17 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techshopapp', '0003_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='techshopapp.item'),
            preserve_default=False,
        ),
    ]
