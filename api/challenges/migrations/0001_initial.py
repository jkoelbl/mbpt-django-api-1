# Generated by Django 2.0.4 on 2018-04-23 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.CharField(max_length=30, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('difficulty', models.FloatField(default=0)),
                ('submission_count', models.PositiveIntegerField(default=0)),
                ('accepted_count', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='api.Tag')),
                ('tier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Tier')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='challenges.Challenge')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='api.Language')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='challenges.SubmissionStatus'),
        ),
    ]
