# Generated by Django 3.0.2 on 2020-03-23 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0002_auto_20200322_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
