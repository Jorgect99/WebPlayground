# Generated by Django 3.1.4 on 2020-12-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
