# Generated by Django 4.0.1 on 2023-05-31 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photo_album')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.category')),
            ],
        ),
    ]
