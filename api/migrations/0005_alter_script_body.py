# Generated by Django 3.2.9 on 2022-01-21 10:43

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_script_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='body',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
