# Generated by Django 4.2.4 on 2023-09-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_remove_todo_name_todo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
