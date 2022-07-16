# Generated by Django 4.0.6 on 2022-07-16 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('habit_name', models.CharField(max_length=150)),
                ('goal', models.PositiveIntegerField(default=0)),
                ('unit', models.CharField(max_length=55)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='HabitTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('goal_quantity', models.PositiveIntegerField(default=0)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habit_trackers', to='habits.habit')),
            ],
        ),
        migrations.AddField(
            model_name='habit',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='habittracker',
            constraint=models.UniqueConstraint(fields=('habit', 'date'), name='unique_entry'),
        ),
    ]