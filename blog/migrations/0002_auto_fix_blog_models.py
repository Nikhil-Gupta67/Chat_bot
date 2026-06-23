from django.db import migrations, models
import django.db.models.deletion
import uuid


def create_legacy_conversation(apps, schema_editor):
    Message = apps.get_model('blog', 'Message')
    Conversation = apps.get_model('blog', 'Conversation')
    if Message.objects.exists():
        conv = Conversation.objects.create(session_id=f'legacy-{uuid.uuid4().hex}')
        Message.objects.filter(conversation__isnull=True).update(conversation=conv)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='blog.Conversation'),
        ),
        migrations.AddField(
            model_name='message',
            name='message_type',
            field=models.CharField(choices=[('user', 'User Message'), ('bot', 'Bot Response')], default='user', max_length=10),
        ),
        migrations.AddField(
            model_name='message',
            name='confidence_score',
            field=models.FloatField(default=0.0, help_text='Bot response confidence (0-1)'),
        ),
        migrations.AddField(
            model_name='message',
            name='is_helpful',
            field=models.BooleanField(blank=True, null=True, help_text='User feedback on response'),
        ),
        migrations.RunPython(create_legacy_conversation, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='blog.Conversation'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['conversation', 'timestamp'], name='blog_message_conversation_idx'),
        ),
        migrations.CreateModel(
            name='BotResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200)),
                ('response', models.TextField()),
                ('category', models.CharField(default='general', max_length=50)),
                ('priority', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('usage_count', models.IntegerField(default=0)),
            ],
            options={'ordering': ['-priority', '-usage_count']},
        ),
        migrations.CreateModel(
            name='ChatFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Good'), (4, '4 - Very Good'), (5, '5 - Excellent')])),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='blog.Message')),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
