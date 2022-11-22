# Generated by Django 4.1.3 on 2022-11-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('s', 'Shirt'), ('sw', 'Sport wear'), ('ow', 'Outwear')], default='S', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=1),
            preserve_default=False,
        ),
    ]
