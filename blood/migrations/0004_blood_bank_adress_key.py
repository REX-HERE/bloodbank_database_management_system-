from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0003_auto_20191121_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood_bank',
            name='adress_key',
            field=models.TextField(default='India'),
        ),
    ]
