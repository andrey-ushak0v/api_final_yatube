# Generated by Django 2.2.16 on 2021-11-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211116_1820'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique pair',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following', 'user'), name='unique pair'),
        ),
    ]