# Generated by Django 4.1.7 on 2023-03-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_Cliente', models.CharField(max_length=100)),
                ('User_Name', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=50)),
                ('Senha', models.CharField(max_length=30)),
            ],
        ),
    ]