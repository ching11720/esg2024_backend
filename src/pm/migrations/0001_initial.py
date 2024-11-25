# Generated by Django 4.2.14 on 2024-10-09 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Boundary",
            fields=[
                (
                    "BID",
                    models.CharField(max_length=11, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=100)),
                ("created_date", models.DateField()),
                ("modified_date", models.DateField()),
            ],
            options={
                "db_table": "boundary",
            },
        ),
        migrations.CreateModel(
            name="DailyRecord",
            fields=[
                ("dailyID", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("runtime", models.FloatField(blank=True, null=True)),
                ("amount", models.FloatField()),
                ("unit", models.CharField(max_length=10)),
                ("created_date", models.DateField()),
                ("last_modified_date", models.DateField()),
            ],
            options={
                "db_table": "daily_record",
            },
        ),
        migrations.CreateModel(
            name="DailyRecordModified",
            fields=[
                (
                    "dailyID_modified",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("date", models.DateField()),
                ("runtime", models.FloatField(blank=True, null=True)),
                ("amount", models.FloatField()),
                ("unit", models.CharField(max_length=10)),
                ("created_date", models.DateField()),
                ("status", models.IntegerField()),
            ],
            options={
                "db_table": "daily_record_modified",
            },
        ),
        migrations.CreateModel(
            name="Emission",
            fields=[
                ("emissionID", models.AutoField(primary_key=True, serialize=False)),
                ("amount_kg", models.FloatField()),
            ],
            options={
                "db_table": "emission",
            },
        ),
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
            name="GreenHouseGas",
            fields=[
                (
                    "GID",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("gwp", models.FloatField()),
            ],
            options={
                "db_table": "green_house_gas",
            },
        ),
        migrations.CreateModel(
            name="PPN",
            fields=[
                (
                    "PN",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("total_amount", models.IntegerField()),
                ("unit", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "product_part_number",
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
                ("flow", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "projects",
            },
        ),
        migrations.CreateModel(
            name="RepairLog",
            fields=[
                ("repairID", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("notes", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "repair_log",
            },
        ),
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "RID",
                    models.CharField(max_length=14, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("amount", models.IntegerField()),
                ("unit", models.CharField(max_length=10)),
                ("purchase_date", models.DateField()),
                ("disposal_date", models.DateField()),
                ("age", models.IntegerField()),
                ("factor", models.FloatField(blank=True, default=0, null=True)),
                ("form", models.CharField(blank=True, max_length=10, null=True)),
                ("category", models.CharField(blank=True, max_length=10, null=True)),
                ("status", models.IntegerField(default=1)),
            ],
            options={
                "db_table": "resource",
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
            name="WorksOn",
            fields=[
                ("workID", models.AutoField(primary_key=True, serialize=False)),
                ("position", models.CharField(max_length=255)),
                ("role_on_sys", models.CharField(max_length=100)),
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
            },
        ),
        migrations.CreateModel(
            name="Usage",
            fields=[
                ("usageID", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.IntegerField()),
                ("unit", models.CharField(max_length=45)),
                (
                    "PID",
                    models.ForeignKey(
                        db_column="PID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.project",
                    ),
                ),
                (
                    "PN",
                    models.ForeignKey(
                        db_column="PN",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pm.ppn",
                    ),
                ),
            ],
            options={
                "db_table": "usage",
            },
        ),
        migrations.AddConstraint(
            model_name="supplier",
            constraint=models.CheckConstraint(
                check=models.Q(("SID__regex", "^05[0-9]{10}$")), name="check_sid_format"
            ),
        ),
        migrations.AddConstraint(
            model_name="supplier",
            constraint=models.CheckConstraint(
                check=models.Q(("phone__regex", "^[0-9]+$")), name="check_sphone_format"
            ),
        ),
        migrations.AddField(
            model_name="resource",
            name="PN",
            field=models.ForeignKey(
                db_column="PN", on_delete=django.db.models.deletion.CASCADE, to="pm.ppn"
            ),
        ),
        migrations.AddField(
            model_name="resource",
            name="SID",
            field=models.ForeignKey(
                db_column="SID",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.supplier",
            ),
        ),
        migrations.AddField(
            model_name="repairlog",
            name="RID",
            field=models.ForeignKey(
                db_column="RID",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.resource",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="BID",
            field=models.ForeignKey(
                db_column="BID",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.boundary",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="PMID",
            field=models.ForeignKey(
                db_column="PMID",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.employee",
            ),
        ),
        migrations.AddConstraint(
            model_name="ppn",
            constraint=models.CheckConstraint(
                check=models.Q(("PN__regex", "^06[0-9]{4}$")), name="check_pn_format"
            ),
        ),
        migrations.AddConstraint(
            model_name="employee",
            constraint=models.CheckConstraint(
                check=models.Q(("EID__regex", "^02[0-9]{10}$")), name="check_eid_format"
            ),
        ),
        migrations.AddConstraint(
            model_name="employee",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "email__regex",
                        "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                    )
                ),
                name="check_email_format",
            ),
        ),
        migrations.AddConstraint(
            model_name="employee",
            constraint=models.CheckConstraint(
                check=models.Q(("phone__regex", "^[0-9]+$")), name="check_phone_format"
            ),
        ),
        migrations.AddConstraint(
            model_name="employee",
            constraint=models.CheckConstraint(
                check=models.Q(("gender__in", [1, 2])), name="employees_chk_1"
            ),
        ),
        migrations.AddField(
            model_name="emission",
            name="GID",
            field=models.ForeignKey(
                db_column="GID",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.greenhousegas",
            ),
        ),
        migrations.AddField(
            model_name="emission",
            name="RID",
            field=models.ForeignKey(
                db_column="RID",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.resource",
            ),
        ),
        migrations.AddField(
            model_name="dailyrecordmodified",
            name="PID",
            field=models.ForeignKey(
                db_column="PID",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.project",
            ),
        ),
        migrations.AddField(
            model_name="dailyrecordmodified",
            name="PN",
            field=models.ForeignKey(
                db_column="PN", on_delete=django.db.models.deletion.CASCADE, to="pm.ppn"
            ),
        ),
        migrations.AddField(
            model_name="dailyrecordmodified",
            name="created_by",
            field=models.ForeignKey(
                db_column="created_by",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.employee",
            ),
        ),
        migrations.AddField(
            model_name="dailyrecordmodified",
            name="dailyID_origin",
            field=models.ForeignKey(
                db_column="dailyID_origin",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.dailyrecord",
            ),
        ),
        migrations.AddField(
            model_name="dailyrecord",
            name="PID",
            field=models.ForeignKey(
                db_column="PID",
                on_delete=django.db.models.deletion.CASCADE,
                to="pm.project",
            ),
        ),
        migrations.AddField(
            model_name="dailyrecord",
            name="PN",
            field=models.ForeignKey(
                db_column="PN", on_delete=django.db.models.deletion.CASCADE, to="pm.ppn"
            ),
        ),
        migrations.AddField(
            model_name="dailyrecord",
            name="created_by",
            field=models.ForeignKey(
                db_column="created_by",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_DailyRecord",
                to="pm.employee",
            ),
        ),
        migrations.AddField(
            model_name="dailyrecord",
            name="last_modified_by",
            field=models.ForeignKey(
                db_column="last_modified_by",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="modified_DailyRecord",
                to="pm.employee",
            ),
        ),
        migrations.AddField(
            model_name="boundary",
            name="created_by",
            field=models.ForeignKey(
                db_column="created_by",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_boundaries",
                to="pm.employee",
            ),
        ),
        migrations.AddField(
            model_name="boundary",
            name="modified_by",
            field=models.ForeignKey(
                db_column="modified_by",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="modified_boundaries",
                to="pm.employee",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="workson",
            unique_together={("EID", "PID")},
        ),
        migrations.AlterUniqueTogether(
            name="usage",
            unique_together={("PID", "PN")},
        ),
        migrations.AddConstraint(
            model_name="resource",
            constraint=models.CheckConstraint(
                check=models.Q(("RID__regex", "^03[0-9]{12}$")), name="check_rid_format"
            ),
        ),
        migrations.AddConstraint(
            model_name="project",
            constraint=models.CheckConstraint(
                check=models.Q(("PID__regex", "^01[0-9]{6}$")), name="check_pid_format"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="emission",
            unique_together={("RID", "GID")},
        ),
        migrations.AlterUniqueTogether(
            name="dailyrecord",
            unique_together={("PID", "PN", "date")},
        ),
        migrations.AddConstraint(
            model_name="boundary",
            constraint=models.CheckConstraint(
                check=models.Q(("BID__regex", "^04[0-9]{9}$")), name="check_bid_format"
            ),
        ),
    ]