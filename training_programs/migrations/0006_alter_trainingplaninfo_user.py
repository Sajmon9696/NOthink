# Generated by Django 4.2.7 on 2024-01-20 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training_programs', '0005_alter_trainingplaninfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingplaninfo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
