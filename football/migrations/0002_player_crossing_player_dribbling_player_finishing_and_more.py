# Generated by Django 5.1.5 on 2025-02-22 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='crossing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='dribbling',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='finishing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='penalties',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='release_clause_euro',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='vision',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
