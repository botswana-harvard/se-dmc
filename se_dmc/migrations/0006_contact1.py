# Generated by Django 3.0.2 on 2020-02-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('se_dmc', '0005_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('sender', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('cc_myself', models.BooleanField(blank=True)),
            ],
        ),
    ]