# Generated by Django 5.1.4 on 2025-01-21 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_bookmarkplace_category_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookmarklist',
            unique_together={('bookmark', 'bookmarkplace'), ('bookmark', 'bookmarkschedule')},
        ),
    ]
