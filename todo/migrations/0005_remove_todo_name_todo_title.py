# Generated by Django 4.2.4 on 2023-09-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='name',
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default='title', max_length=100),
            preserve_default=False,
        ),
    ]