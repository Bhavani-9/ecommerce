# Generated by Django 2.2.4 on 2020-05-11 03:16

from core import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(help_text='Size: 1920x570', upload_to=''),
        ),
    ]
