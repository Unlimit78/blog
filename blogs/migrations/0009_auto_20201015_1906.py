# Generated by Django 3.1.2 on 2020-10-15 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='blog',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog', to='blogs.blog'),
        ),
    ]
