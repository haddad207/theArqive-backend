# Generated by Django 2.2.7 on 2020-03-01 23:33

from django.db import migrations, models
import django.db.models.deletion
import pins.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='categoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=50)),
                ('image_url', models.ImageField(null=True, upload_to=pins.models.categoryType.upload_photo_dir)),
            ],
        ),
        migrations.CreateModel(
            name='commentStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_anonymous_comment', models.BooleanField(default=False)),
                ('description', models.TextField()),
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
        migrations.CreateModel(
            name='flagStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flagged', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.ImageField(null=True, upload_to=pins.models.photo.upload_photo_dir)),
            ],
        ),
        migrations.CreateModel(
            name='pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('upVotes', models.PositiveSmallIntegerField(default=0)),
                ('startDate', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('endDate', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('is_anonymous_pin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='upVoteStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.BooleanField(default=False)),
                ('pinId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updotes', to='pins.pin')),
            ],
        ),
    ]
