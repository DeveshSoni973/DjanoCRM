# Generated by Django 5.0.6 on 2024-06-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
