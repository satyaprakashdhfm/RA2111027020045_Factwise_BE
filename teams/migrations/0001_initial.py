# Generated by Django 4.0.3 on 2022-04-03 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('creationtime', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='users.user')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='users.user')),
            ],
        ),
    ]
