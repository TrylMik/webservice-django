# Generated by Django 4.0.5 on 2022-06-13 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_spotscomment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotscomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spots_comments', to='main.spotspost'),
        ),
    ]
