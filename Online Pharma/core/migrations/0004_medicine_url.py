# Generated by Django 3.1.5 on 2021-07-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201222_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='url',
            field=models.URLField(default='https://veganfoodandliving-1321f.kxcdn.com/wp-content/uploads/2019/03/featured.jpg'),
        ),
    ]
