# Generated by Django 4.0.4 on 2022-05-02 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_section_dummy_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='dummy_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dummy', to='query.course'),
        ),
    ]
