# Generated by Django 4.2.11 on 2024-04-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='full_name',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
