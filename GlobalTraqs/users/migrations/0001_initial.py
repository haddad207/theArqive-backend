# Generated by Django 2.2.7 on 2020-02-27 03:53

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Last Name')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Username')),
                ('email', models.CharField(blank=True, max_length=70, unique=True, verbose_name='Email')),
                ('is_moderator', models.BooleanField(default=False)),
                ('is_administrator', models.BooleanField(default=False)),
                ('is_anonymous_active', models.BooleanField(default=False)),
                ('accessibility_mode_active', models.BooleanField(default=False)),
                ('bio', models.CharField(blank=True, max_length=300)),
                ('is_profile_private', models.BooleanField(default=False)),
                ('image_url', models.ImageField(null=True, upload_to=users.models.User.upload_photo_dir)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('can_add_stories', 'Can add stories'), ('can_edit_their_stories', 'Can edit their stories'), ('can_delete_their_stories', 'Can delete their stories'), ('can_delete_other_stories', 'Can delete other user stories'), ('can_edit_other_stories', 'Can edit other user stories'), ('can_ban_users', 'Can ban users'), ('can_ban_moderators', 'Can ban moderators'), ('can_add_moderators', 'Can add moderators'), ('can_add_admin', 'Can add administrators'), ('can_add_personal_stories', 'Can add personal stories')),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
