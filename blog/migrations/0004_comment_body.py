# Generated by Django 4.1.1 on 2022-11-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_comment_blog_commen_created_0e6ed4_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default=''),
        ),
    ]
