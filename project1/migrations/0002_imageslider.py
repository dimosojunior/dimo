# Generated by Django 3.2.5 on 2021-07-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/%y')),
                ('caption', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
    ]