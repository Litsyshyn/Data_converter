# Generated by Django 3.0.7 on 2020-06-16 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0010_auto_20200611_1348_squashed_0013_foundernew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='edrpou',
            field=models.CharField(db_index=True, max_length=260),
        ),
        migrations.AlterField(
            model_name='foundernew',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='founders_new', to='business_register.Company'),
        ),
        migrations.AlterField(
            model_name='historicalcompany',
            name='edrpou',
            field=models.CharField(db_index=True, max_length=260),
        ),
    ]
