# Generated by Django 4.0 on 2023-10-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='trello_account',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Трелло-аккаунт'),
        ),
    ]
