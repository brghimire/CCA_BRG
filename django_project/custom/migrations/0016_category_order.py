# Generated by Django 2.2.16 on 2021-05-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0015_category_boundary_layer'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]