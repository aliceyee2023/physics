# Generated by Django 3.2.1 on 2024-05-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=75)),
                ('Level', models.CharField(max_length=10)),
                ('Course', models.CharField(max_length=30)),
                ('Preferred_Timing', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
