# Generated by Django 2.2.6 on 2019-11-17 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20191116_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('año', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['nombre', 'modelo'],
            },
        ),
    ]
