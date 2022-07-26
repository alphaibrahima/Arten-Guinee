# Generated by Django 2.1.5 on 2021-02-15 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EvenementAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='even_images')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('archive', models.BooleanField(default=False)),
                ('titre', models.CharField(max_length=255)),
                ('lieu', models.CharField(max_length=255)),
                ('Date', models.DateTimeField()),
                ('contenu', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
