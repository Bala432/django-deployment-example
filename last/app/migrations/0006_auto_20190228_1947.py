# Generated by Django 2.1.5 on 2019-02-28 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190228_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userpost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='app.UserInfo'),
        ),
    ]