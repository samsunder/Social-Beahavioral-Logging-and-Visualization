# Generated by Django 2.1.1 on 2018-09-20 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign1', '0005_eventslog'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time1', models.DateTimeField()),
                ('time2', models.DateTimeField()),
                ('time3', models.DateTimeField()),
            ],
        ),
    ]
