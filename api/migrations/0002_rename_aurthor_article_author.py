# Generated by Django 3.2.5 on 2021-10-02 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='aurthor',
            new_name='author',
        ),
    ]
