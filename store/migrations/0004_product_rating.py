# Generated by Django 4.0.5 on 2022-07-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.PositiveIntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True),
        ),
    ]
