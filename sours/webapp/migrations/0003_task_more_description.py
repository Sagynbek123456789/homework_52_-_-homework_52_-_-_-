from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_task_date_of_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='more_description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Подробное описание'),
        ),
    ]
