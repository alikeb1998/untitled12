# Generated by Django 3.1.1 on 2020-09-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apifirst', '0002_animals'),
    ]

    operations = [
        migrations.CreateModel(
            name='mamada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=300)),
                ('date', models.DateTimeField(verbose_name='auto_now_add=true')),
            ],
        ),
    ]
