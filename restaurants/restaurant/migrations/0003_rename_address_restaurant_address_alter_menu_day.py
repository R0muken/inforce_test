# Generated by Django 4.1 on 2022-09-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_menu_menu_restaurant_restaurant_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='Address',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='menu',
            name='day',
            field=models.IntegerField(choices=[(0, 'day'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Sunday'), (7, 'Saturday')], default=0),
        ),
    ]
