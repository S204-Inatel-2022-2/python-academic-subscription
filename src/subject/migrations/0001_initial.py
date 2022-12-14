# Generated by Django 4.1 on 2022-09-28 23:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_slug', models.CharField(max_length=50)),
                ('total_hour', models.IntegerField()),
                ('credits', models.IntegerField()),
            ],
        ),
    ]
