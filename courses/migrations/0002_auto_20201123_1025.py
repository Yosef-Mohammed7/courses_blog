# Generated by Django 3.0.9 on 2020-11-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titl', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='lendet',
            name='klasa',
        ),
        migrations.RemoveField(
            model_name='lendet',
            name='krijues',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='lenda',
        ),
        migrations.DeleteModel(
            name='Klasa',
        ),
        migrations.DeleteModel(
            name='Lendet',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
    ]
