# Generated by Django 2.2.8 on 2020-07-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200702_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('TS', 'Tshirt'), ('SK', 'Sneaker'), ('WH', 'Watch'), ('HB', 'Handbag'), ('JS', 'Jeans')], max_length=2),
        ),
    ]
