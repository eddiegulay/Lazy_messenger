# Generated by Django 3.2.4 on 2022-01-08 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_user', to='accounts.profile')),
                ('last_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('notification_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_owner', to='accounts.profile')),
                ('notification_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='MyChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chat')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('time_sent', models.DateField(auto_now=True)),
                ('text', models.BooleanField(default=True)),
                ('image', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('chat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chat')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_host', to='accounts.profile')),
            ],
        ),
    ]
