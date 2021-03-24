# Generated by Django 3.0.7 on 2021-03-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0074_auto_20210323_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companylinkwithpep',
            name='confirmation_date',
            field=models.DateField(help_text='Date of confirmation of connection in the "Anti-Corruption Action Center" database.', null=True, verbose_name='connection`s confirmation date'),
        ),
        migrations.AlterField(
            model_name='companylinkwithpep',
            name='end_date',
            field=models.DateField(help_text='Date of termination of connection between the person and  this company', null=True, verbose_name='connection`s end date'),
        ),
        migrations.AlterField(
            model_name='companylinkwithpep',
            name='start_date',
            field=models.DateField(help_text="Date of the beginning of the person's connection with the company.", null=True, verbose_name='connection`s start date'),
        ),
        migrations.AlterField(
            model_name='relatedpersonslink',
            name='confirmation_date',
            field=models.DateField(help_text='Date of confirmation of connection in the "Anti-Corruption Action Center" database.', null=True, verbose_name='connection`s confirmation date'),
        ),
        migrations.AlterField(
            model_name='relatedpersonslink',
            name='end_date',
            field=models.DateField(help_text='The date the relationship ends.', null=True, verbose_name='connection`s end date'),
        ),
        migrations.AlterField(
            model_name='relatedpersonslink',
            name='start_date',
            field=models.DateField(help_text='Date of the beginning of the relationship.', null=True, verbose_name='connection`s start date'),
        ),
    ]
