from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('email', models.CharField(max_length=120)),
                ('contact', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=220)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
