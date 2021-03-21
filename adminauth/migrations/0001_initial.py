# Generated by Django 3.0.5 on 2021-02-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminauthModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_email', models.EmailField(max_length=255)),
                ('admin_password', models.CharField(max_length=255)),
                ('profile_pic', models.ImageField(null=True, upload_to='profile_pic/', verbose_name='Profile Pic')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
