# Generated by Django 5.1.2 on 2024-10-15 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_create_data_alter_post_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
