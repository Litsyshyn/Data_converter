# Generated by Django 3.0.7 on 2021-03-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0038_auto_20210305_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsubscription',
            name='duration',
            field=models.PositiveIntegerField(verbose_name='profits', default=30),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='projectsubscription',
            name='duration',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='duration',
            field=models.PositiveIntegerField(verbose_name='profits', default=30),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='duration',
        ),
        migrations.AddField(
            model_name='projectsubscription',
            name='periodicity',
            field=models.CharField(choices=[('month', 'Month'), ('year', 'Year')], default='month', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectsubscription',
            name='start_day',
            field=models.SmallIntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='periodicity',
            field=models.CharField(choices=[('month', 'Month'), ('year', 'Year')], default='month', help_text='days', max_length=5),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='is_custom',
            field=models.BooleanField(blank=True, default=False, help_text='Custom subscription not shown to users', verbose_name='is custom'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='is_default',
            field=models.BooleanField(blank=True, default=False, verbose_name='is default'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='platform_requests_limit',
            field=models.IntegerField(help_text='Limit for API requests from the project via platform', verbose_name='platform requests limit'),
        ),
    ]