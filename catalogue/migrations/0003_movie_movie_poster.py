# Generated by Django 4.2.5 on 2023-10-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_actor_actor_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_poster',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Movie poster:'),
        ),
    ]