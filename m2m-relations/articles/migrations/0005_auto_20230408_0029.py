# Generated by Django 3.1.2 on 2023-04-07 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20230408_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='scopes',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article', verbose_name='Статья'),
        ),
    ]
