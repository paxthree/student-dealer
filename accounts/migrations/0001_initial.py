# Generated by Django 2.0.1 on 2018-02-28 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('uni', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
