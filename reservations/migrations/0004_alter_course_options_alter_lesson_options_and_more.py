# Generated by Django 4.2.7 on 2024-03-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_participant_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Kurz', 'verbose_name_plural': 'Kurzy'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Lekce', 'verbose_name_plural': 'Lekce'},
        ),
        migrations.AlterModelOptions(
            name='participant',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='course',
            name='password',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]