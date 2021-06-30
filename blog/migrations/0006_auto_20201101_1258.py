# Generated by Django 3.1 on 2020-11-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201101_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valueofsplitedata',
            name='battery',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='valueofsplitedata',
            name='bcurrent',
            field=models.FloatField(default=0, max_length=9),
        ),
        migrations.AlterField(
            model_name='valueofsplitedata',
            name='bvolt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='valueofsplitedata',
            name='rcurrent',
            field=models.FloatField(default=0, max_length=9),
        ),
        migrations.AlterField(
            model_name='valueofsplitedata',
            name='rvolt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='valueofsplitedata',
            name='ycurrent',
            field=models.FloatField(default=0, max_length=9),
        ),
        migrations.AlterField(
            model_name='valueofsplitedata',
            name='yvolt',
            field=models.IntegerField(default=0),
        ),
    ]
