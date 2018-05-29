# Generated by Django 2.0.5 on 2018-05-29 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('chapter', models.PositiveIntegerField()),
                ('post_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('user', models.CharField(max_length=25)),
                ('post_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=25)),
                ('body', models.TextField()),
                ('post_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=25)),
                ('body', models.TextField()),
                ('post_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='prompt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='storytimes.Prompt'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='storytimes.Post'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='storytimes.Post'),
        ),
    ]
