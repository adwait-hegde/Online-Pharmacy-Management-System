# Generated by Django 3.0.3 on 2020-10-10 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_address', models.CharField(default='', max_length=100)),
                ('street_address', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('zip', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Address')),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='pharmacy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pharmacy'),
        ),
    ]
