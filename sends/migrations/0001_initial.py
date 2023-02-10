# Generated by Django 4.1.5 on 2023-02-09 12:20

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
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_mail', models.EmailField(max_length=255)),
                ('client_name', models.CharField(max_length=255)),
                ('client_comm', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mails', models.TextField()),
                ('letter_time', models.TimeField()),
                ('letter_periood', models.CharField(choices=[('day', 'day'), ('week', 'week'), ('month', 'month')], default='day', max_length=10)),
                ('msg_title', models.CharField(max_length=255, verbose_name='Message Title')),
                ('msg_body', models.TextField(max_length=1000, verbose_name='Message Body')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_title', models.CharField(max_length=255)),
                ('msg_body', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_time', models.TimeField()),
                ('letter_periood', models.CharField(choices=[('day', 'day'), ('week', 'week'), ('month', 'month')], default='day', max_length=10)),
                ('letter_status', models.CharField(choices=[('created', 'created'), ('completed', 'completed'), ('started', 'started')], default='started', max_length=10)),
                ('letter_clients', models.TextField(blank=True, null=True)),
                ('letter_mails', models.TextField(blank=True, null=True)),
                ('letter_message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sends.message')),
                ('letter_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Try_Send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('try_time', models.DateTimeField(auto_now_add=True)),
                ('try_status', models.BooleanField(default=True)),
                ('try_reply', models.TextField(blank=True, null=True)),
                ('try_newsletter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sends.newsletter')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coll_clients', models.TextField()),
                ('coll_message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sends.message')),
                ('coll_newsletter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sends.newsletter')),
            ],
        ),
    ]
