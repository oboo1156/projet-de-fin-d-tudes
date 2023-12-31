# Generated by Django 4.1.6 on 2023-02-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("counsel", "0002_alter_client_options_alter_comment_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"ordering": ("-date", "hashtag")},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ("-date",)},
        ),
        migrations.AlterModelOptions(
            name="commentreply",
            options={"ordering": ("-date",)},
        ),
        migrations.RemoveField(
            model_name="comment",
            name="time",
        ),
        migrations.RemoveField(
            model_name="commentreply",
            name="time",
        ),
        migrations.AddField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="commentreply",
            name="date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="hashtag",
            field=models.CharField(
                choices=[
                    ("education", "educative"),
                    ("gossip", "gossip"),
                    ("creating", "creating"),
                    ("hawt", "hawt"),
                    ("sad", "sad"),
                    ("relationship", "relationship"),
                    ("interesting", "interesting"),
                    ("funny", "funny"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="hashtagg",
            field=models.CharField(
                choices=[
                    ("education", "educative"),
                    ("gossip", "gossip"),
                    ("creating", "creating"),
                    ("hawt", "hawt"),
                    ("sad", "sad"),
                    ("relationship", "relationship"),
                    ("interesting", "interesting"),
                    ("funny", "funny"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="counsellor",
            name="date",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
