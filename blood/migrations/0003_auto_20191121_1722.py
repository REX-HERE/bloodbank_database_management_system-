from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0002_blood_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_bank',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
