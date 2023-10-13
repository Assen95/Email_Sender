# Generated by Django 4.2.5 on 2023-10-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=25)),
                ('to_email', models.EmailField(max_length=30)),
                ('content', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]