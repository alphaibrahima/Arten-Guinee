# Generated by Django 2.1.5 on 2020-11-04 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Competence', '0001_initial'),
        ('utilisateurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compentence',
            name='profil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.Profile'),
        ),
        migrations.AddField(
            model_name='compentence',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
