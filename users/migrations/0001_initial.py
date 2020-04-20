# Generated by Django 3.0.5 on 2020-04-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(upload_to='')),
                ('first_name', models.CharField(max_length=128)),
                ('second_name', models.CharField(max_length=128)),
                ('age', models.SmallIntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
            ],
        ),
    ]