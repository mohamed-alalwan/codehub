# Generated by Django 4.1.7 on 2023-03-18 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_profile_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.category'),
        ),
    ]
