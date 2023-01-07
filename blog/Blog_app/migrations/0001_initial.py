# Generated by Django 4.1.1 on 2022-09-21 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_title', models.CharField(max_length=267, verbose_name='Put a Title')),
                ('Slug', models.SlugField(max_length=267, unique=True)),
                ('Blog_content', models.TextField()),
                ('Blog_image', models.ImageField(upload_to='Blog_image')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('Update_date', models.DateTimeField(auto_now=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog_app.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('Comment_date', models.DateTimeField(auto_now_add=True)),
                ('Blog_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog_app.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]