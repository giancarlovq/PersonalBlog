# Generated by Django 2.2.7 on 2019-12-31 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191231_0224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Publications'},
        ),
    ]
