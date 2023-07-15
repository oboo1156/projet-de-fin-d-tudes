# Generated by Django 4.1.6 on 2023-02-23 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("counsel", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"ordering": ("-date", "-time", "hashtag")},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ("-time",)},
        ),
        migrations.AddField(
            model_name="client",
            name="hashtag",
            field=models.CharField(
                choices=[
                    ("education", "edu"),
                    ("gossip", "goss"),
                    ("creating", "creat"),
                    ("hawt", "ho"),
                    ("sad", "sa"),
                    ("relationship", "relat"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="hashtagg",
            field=models.CharField(
                choices=[
                    ("education", "edu"),
                    ("gossip", "goss"),
                    ("creating", "creat"),
                    ("hawt", "ho"),
                    ("sad", "sa"),
                    ("relationship", "relat"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="time",
            field=models.TimeField(null=True),
        ),
        migrations.CreateModel(
            name="CommentReply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.TimeField(null=True)),
                ("reply", models.TextField(null=True)),
                (
                    "comment",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="counsel.comment",
                    ),
                ),
            ],
            options={
                "ordering": ("-time",),
            },
        ),
    ]
