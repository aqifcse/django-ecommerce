# Generated by Django 2.2.8 on 2020-07-06 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200705_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
