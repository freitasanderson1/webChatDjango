# Generated by Django 5.1.2 on 2024-10-22 07:03

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Criação')),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
                'ordering': ['dataCriacao'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dataAniversario', models.DateField(null=True, verbose_name='Data de Aniversário')),
                ('imagemPerfil', models.ImageField(blank=True, upload_to='Perfil')),
                ('imagemCapa', models.ImageField(blank=True, upload_to='Capa')),
                ('qtdSeguindo', models.IntegerField(default=0, verbose_name='Quantidade Seguindo')),
                ('qtdSeguidores', models.IntegerField(default=0, verbose_name='Quantidade Seguidores')),
                ('groups', models.ManyToManyField(blank=True, help_text='Os grupos aos quais este usuário pertence.', related_name='usuario_set', related_query_name='usuario', to='auth.group', verbose_name='Grupos de Permissões')),
                ('seguidores', models.ManyToManyField(blank=True, related_name='Seguidores', to='webchat.usuario')),
                ('seguindo', models.ManyToManyField(blank=True, related_name='Seguindo', to='webchat.usuario')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Permissões específicas para este usuário.', related_name='usuario_permissions', related_query_name='usuario', to='auth.permission', verbose_name='Permissões de Usuários')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField(default=' ', max_length=2800, verbose_name='Conteúdo da Mensagem')),
                ('dataEnvio', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Envio')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webchat.chat', verbose_name='Chat')),
                ('quemEnviou', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quemEnviou', to='webchat.usuario', verbose_name='Quem enviou')),
                ('quemLeu', models.ManyToManyField(related_name='quemLeu', to='webchat.usuario', verbose_name='Usuários que leram')),
                ('quemRecebeu', models.ManyToManyField(related_name='quemRecebeu', to='webchat.usuario', verbose_name='Usuários que receberam')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['dataEnvio', 'chat'],
            },
        ),
        migrations.AddField(
            model_name='chat',
            name='usuarios',
            field=models.ManyToManyField(to='webchat.usuario', verbose_name='Usuários no Chat'),
        ),
    ]
