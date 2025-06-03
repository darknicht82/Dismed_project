from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departamentos",
            fields=[
                ("iddepto", models.AutoField(primary_key=True, serialize=False)),
                ("nombredept", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "departamentos",
            },
        ),
    ]
