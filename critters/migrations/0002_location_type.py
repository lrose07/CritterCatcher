# Generated by Django 3.1.1 on 2020-09-07 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('critters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='critters.crittertype'),
            preserve_default=False,
        ),
    ]
