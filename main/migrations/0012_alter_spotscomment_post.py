# Generated by Django 4.0.5 on 2022-06-13 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_spotscomment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotscomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spotscomments', to='main.spotspost'),
        ),
    ]
