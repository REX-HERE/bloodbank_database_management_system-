from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0006_blood_camps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateblood',
            name='blood_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood.AvailableBloodGroups'),
        ),
        migrations.AlterField(
            model_name='donateblood',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood.AvailableCity'),
        ),
        migrations.AlterField(
            model_name='needblood',
            name='blood_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood.AvailableBloodGroups'),
        ),
        migrations.AlterField(
            model_name='needblood',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood.AvailableCity'),
        ),
    ]
