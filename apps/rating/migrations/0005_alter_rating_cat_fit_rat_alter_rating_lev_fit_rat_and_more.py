# Generated by Django 4.2.4 on 2023-08-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rating", "0004_alter_rating_cat_fit_rat_alter_rating_lev_fit_rat_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="cat_fit_rat",
            field=models.CharField(
                choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="lev_fit_rat",
            field=models.CharField(
                choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="rating",
            field=models.IntegerField(),
        ),
    ]
