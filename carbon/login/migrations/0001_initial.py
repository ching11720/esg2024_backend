# Generated by Django 4.2.11 on 2024-05-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Act",
            fields=[
                (
                    "act_id",
                    models.IntegerField(
                        db_column="ACT_ID", primary_key=True, serialize=False
                    ),
                ),
                ("act_name", models.CharField(db_column="ACT_NAME", max_length=45)),
                ("category", models.IntegerField(db_column="CATEGORY")),
                ("type", models.CharField(db_column="TYPE", max_length=5)),
                ("act_hour", models.IntegerField(db_column="ACT_HOUR")),
            ],
            options={
                "db_table": "ACT",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ActFac",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("es_no", models.IntegerField(db_column="ES_NO")),
                ("act_no", models.IntegerField(db_column="ACT_NO")),
                ("amount", models.IntegerField(db_column="AMOUNT")),
            ],
            options={
                "db_table": "ACT_FAC",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Ef",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ef_no", models.IntegerField(db_column="EF_NO")),
                ("gas_no", models.IntegerField(db_column="GAS_NO")),
                ("amount", models.IntegerField(db_column="AMOUNT")),
            ],
            options={
                "db_table": "EF",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Es",
            fields=[
                (
                    "es_id",
                    models.IntegerField(
                        db_column="ES_ID", primary_key=True, serialize=False
                    ),
                ),
                ("es_name", models.CharField(db_column="ES_NAME", max_length=45)),
            ],
            options={
                "db_table": "ES",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Gwps",
            fields=[
                (
                    "gas_id",
                    models.IntegerField(
                        db_column="GAS_ID", primary_key=True, serialize=False
                    ),
                ),
                ("gas_name", models.CharField(db_column="GAS_NAME", max_length=45)),
                ("gwps", models.IntegerField(db_column="GWPS")),
            ],
            options={
                "db_table": "GWPS",
                "managed": False,
            },
        ),
    ]
