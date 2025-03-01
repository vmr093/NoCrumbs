# Generated by Django 5.1.6 on 2025-02-27 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='added_at',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.CharField(blank=True, help_text='Comma-separated tags', max_length=200),
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.category'),
        ),
    ]
