# Generated by Django 4.2.14 on 2024-08-11 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "EID",
                    models.CharField(max_length=12, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("gender", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=11)),
                ("nation", models.CharField(max_length=255)),
                ("status", models.IntegerField(default=1)),
            ],
            options={
                "db_table": "employees",
            },
        ),
        migrations.CreateModel(
            name="Equipment",
            fields=[
                (
                    "EQID",
                    models.CharField(max_length=12, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("amount", models.IntegerField()),
                ("unit", models.CharField(max_length=10)),
                ("coefficient", models.FloatField(blank=True, null=True)),
                ("purchase_date", models.DateField()),
                ("disposal_date", models.DateField()),
                ("age", models.IntegerField()),
                ("status", models.IntegerField(default=1)),
            ],
            options={
                "db_table": "equipments",
            },
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "MID",
                    models.CharField(max_length=14, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("amount", models.IntegerField()),
                ("unit", models.CharField(max_length=10)),
                ("coefficient", models.FloatField(blank=True, null=True)),
                ("purchase_date", models.DateField()),
                ("age", models.IntegerField()),
            ],
            options={
                "db_table": "materials",
            },
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "SID",
                    models.CharField(max_length=12, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=11)),
                ("nation", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "suppliers",
            },
        ),
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=255)),
                ("access", models.CharField(max_length=255)),
                (
                    "UID",
                    models.OneToOneField(
                        db_column="UID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.employee",
                    ),
                ),
            ],
            options={
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="Supply",
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
                (
                    "EQID",
                    models.ForeignKey(
                        blank=True,
                        db_column="EQID",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pm.equipment",
                    ),
                ),
                (
                    "MID",
                    models.ForeignKey(
                        blank=True,
                        db_column="MID",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pm.material",
                    ),
                ),
                (
                    "SID",
                    models.ForeignKey(
                        db_column="SID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.supplier",
                    ),
                ),
            ],
            options={
                "db_table": "supply",
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "PID",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("pname", models.CharField(max_length=255)),
                ("flow", models.TextField()),
                (
                    "PMID",
                    models.ForeignKey(
                        db_column="PMID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.user",
                        to_field="UID",
                    ),
                ),
            ],
            options={
                "db_table": "projects",
            },
        ),
        migrations.CreateModel(
            name="WorksOn",
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
                ("position", models.CharField(max_length=255)),
                (
                    "EID",
                    models.ForeignKey(
                        db_column="EID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.employee",
                    ),
                ),
                (
                    "PID",
                    models.ForeignKey(
                        db_column="PID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.project",
                    ),
                ),
            ],
            options={
                "db_table": "works_on",
                "unique_together": {("EID", "PID")},
            },
        ),
        migrations.CreateModel(
            name="UsageM",
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
                ("amount", models.IntegerField(default=1)),
                ("unit", models.CharField(default="unit", max_length=45)),
                (
                    "MID",
                    models.ForeignKey(
                        db_column="MID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.material",
                    ),
                ),
                (
                    "PID",
                    models.ForeignKey(
                        db_column="PID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.project",
                    ),
                ),
            ],
            options={
                "db_table": "usage_m",
                "unique_together": {("PID", "MID")},
            },
        ),
        migrations.CreateModel(
            name="UsageEq",
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
                ("amount", models.IntegerField(default=1)),
                ("unit", models.CharField(default="unit", max_length=45)),
                (
                    "EQID",
                    models.ForeignKey(
                        db_column="EQID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.equipment",
                    ),
                ),
                (
                    "PID",
                    models.ForeignKey(
                        db_column="PID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.project",
                    ),
                ),
            ],
            options={
                "db_table": "usage_eq",
                "unique_together": {("EQID", "PID")},
            },
        ),
    ]
