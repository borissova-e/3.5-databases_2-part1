# Generated by Django 3.1.2 on 2021-01-10 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210108_0802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescope',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематика статей'},
        ),
        migrations.RenameField(
            model_name='scope',
            old_name='article',
            new_name='articles',
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_topic', to='articles.scope', verbose_name='Раздел'),
        ),
    ]