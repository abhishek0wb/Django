# Generated by Django 5.0.2 on 2024-03-03 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_alter_student_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(default=datetime.datetime(2024, 3, 3, 17, 29, 18, 871308, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
