# Generated by Django 4.0.4 on 2022-05-02 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='dummy_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dummy', to='query.course'),
        ),
    ]
