from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0009_chart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='height',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chart',
            name='man',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chart',
            name='woman',
            field=models.CharField(max_length=100),
        ),
    ]
