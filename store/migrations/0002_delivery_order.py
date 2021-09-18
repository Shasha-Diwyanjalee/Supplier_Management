from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('quantity', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete')], max_length=10)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Supplier')),
            ],
        ),
    ]
