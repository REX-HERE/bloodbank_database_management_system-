from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableBloodGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DonateBlood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('donorname', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NeedBlood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('requestname', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
    ]
