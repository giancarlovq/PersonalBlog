# Generated by Django 2.2.7 on 2019-12-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191227_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.ImageField(upload_to='publication/images/'),
        ),
    ]