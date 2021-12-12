# Generated by Django 3.2.7 on 2021-12-11 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0005_sale_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]