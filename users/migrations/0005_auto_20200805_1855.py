# Generated by Django 3.0.8 on 2020-08-05 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200805_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='prof_impacts',
            new_name='impacts',
        ),
    ]
