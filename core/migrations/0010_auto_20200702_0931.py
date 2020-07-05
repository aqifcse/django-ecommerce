# Generated by Django 2.2.8 on 2020-07-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_article_previous'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='previous',
            new_name='previous_article',
        ),
        migrations.AddField(
            model_name='article',
            name='next_article',
            field=models.OneToOneField(blank=True, null=True, on_delete=None, related_name='next_post', to='core.Article'),
        ),
    ]