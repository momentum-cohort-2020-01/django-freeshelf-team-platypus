# Generated by Django 3.0.3 on 2020-02-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_merge_20200228_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='categrory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
