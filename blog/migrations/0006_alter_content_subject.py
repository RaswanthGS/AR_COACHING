# Generated by Django 4.0.5 on 2022-08-01 06:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_content_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='subject',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]