# Generated by Django 3.0.6 on 2020-05-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_question_quizz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quizz',
            field=models.ManyToManyField(to='core.Quizz', verbose_name='Quizz'),
        ),
    ]
