# Generated by Django 3.0.8 on 2020-08-06 08:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0007_auto_20200806_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
