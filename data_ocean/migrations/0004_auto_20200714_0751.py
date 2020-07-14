# Generated by Django 3.0.7 on 2020-07-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_ocean', '0003_auto_20200618_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='data_ocean_list',
            field=models.URLField(default='api/{model_name}/', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='data_ocean_retrieve',
            field=models.URLField(default='api/{model_name}/{id}', max_length=500),
            preserve_default=False,
        ),
    ]
