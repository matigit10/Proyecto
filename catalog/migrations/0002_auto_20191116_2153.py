# Generated by Django 2.2.6 on 2019-11-17 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('image', models.ImageField(upload_to='component', verbose_name='Imagen')),
                ('btnUP', models.CharField(max_length=200, verbose_name='Url_boton')),
                ('imgUp', models.CharField(max_length=200, verbose_name='Url_imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
