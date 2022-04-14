from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0008_auto_20191122_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(max_length=10)),
                ('man', models.CharField(max_length=10)),
                ('woman', models.CharField(max_length=10)),
            ],
        ),
    ]
