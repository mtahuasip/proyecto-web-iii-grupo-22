# Generated by Django 5.2.1 on 2025-06-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0002_remove_libro_id_libro_libro_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='libro_id',
            new_name='id',
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='costo',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
