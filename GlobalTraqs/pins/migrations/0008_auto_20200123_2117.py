# Generated by Django 2.2.7 on 2020-01-24 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pins.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0007_merge_20200123_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutDesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faqQuestionDesc', models.TextField()),
                ('faqAnswerDesc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='categorytype',
            name='image_url',
            field=models.ImageField(null=True, upload_to=pins.models.categoryType.upload_photo_dir),
        ),
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.ImageField(null=True, upload_to=pins.models.photo.upload_photo_dir)),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]