# Generated by Django 5.1.7 on 2025-03-23 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Memeseum_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
