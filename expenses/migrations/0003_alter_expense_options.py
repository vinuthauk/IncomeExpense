# Generated by Django 4.0.5 on 2022-06-22 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_rename_expenses_expense'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
    ]
