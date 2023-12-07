from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_of_completion',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]
