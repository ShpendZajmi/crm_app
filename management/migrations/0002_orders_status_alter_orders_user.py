# Generated by Django 4.0.3 on 2022-03-19 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Status',
            field=models.CharField(choices=[('1', 'INITIAL'), ('2', 'IN_PROGRESS'), ('3', 'COMPLETED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
