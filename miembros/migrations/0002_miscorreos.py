# Generated by Django 4.2.2 on 2023-08-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MisCorreos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remitente', models.CharField(max_length=100, null=True)),
                ('asunto', models.CharField(max_length=100, null=True)),
                ('cuerpo', models.CharField(max_length=1000, null=True)),
                ('otros', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
