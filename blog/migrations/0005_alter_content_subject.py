# Generated by Django 4.0.5 on 2022-08-01 05:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='subject',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
