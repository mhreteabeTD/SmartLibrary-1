# Generated by Django 3.2.23 on 2024-01-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0002_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='location',
        ),
        migrations.AddField(
            model_name='book',
            name='shelves',
            field=models.ManyToManyField(related_name='books', to='bookmanager.Shelf'),
        ),
        migrations.AlterField(
            model_name='shelf',
            name='shelf_number',
            field=models.CharField(max_length=100),
        ),
    ]
