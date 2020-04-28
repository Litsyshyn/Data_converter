# Generated by Django 2.0.9 on 2020-04-28 06:53

from django.db import migrations, models
import django.db.models.deletion


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# ratu.migrations.0036_auto_20200422_1225

class Migration(migrations.Migration):

    replaces = [('ratu', '0036_auto_20200422_1225'), ('ratu', '0037_auto_20200423_1237'), ('ratu', '0038_auto_20200423_1406'), ('ratu', '0039_auto_20200424_0814'), ('ratu', '0040_auto_20200424_1005')]

    dependencies = [
        ('ratu', '0035_auto_20200422_1059'),
    ]

    operations = [
        migrations.RunPython(
            code=ratu.migrations.0036_auto_20200422_1225.Migration.add_kved_not_found,
        ),
        migrations.AlterField(
            model_name='kzed',
            name='name',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='ruo',
            name='kved',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratu.Kzed'),
        ),
        migrations.AlterField(
            model_name='kzed',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.RemoveField(
            model_name='kzed',
            name='division',
        ),
        migrations.RemoveField(
            model_name='kzed',
            name='group',
        ),
        migrations.RemoveField(
            model_name='kzed',
            name='section',
        ),
        migrations.AddField(
            model_name='kved',
            name='code',
            field=models.CharField(default=1, max_length=5, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kved',
            name='division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ratu.Division'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kved',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ratu.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kved',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ratu.Section'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kved',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ruo',
            name='kved',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratu.Kved'),
        ),
        migrations.DeleteModel(
            name='Kzed',
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='kved',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
