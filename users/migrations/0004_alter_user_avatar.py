# Generated by Django 3.2.21 on 2023-10-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='images/users/avatar/defolt/defolt_avatar.png', null=True, upload_to='images/users/avatar/'),
        ),
    ]