# Generated by Django 4.2.3 on 2023-07-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='my_image')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
