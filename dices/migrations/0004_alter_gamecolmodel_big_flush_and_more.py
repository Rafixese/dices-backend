# Generated by Django 4.2.4 on 2023-09-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dices', '0003_gamecolmodel_game_fk_alter_gamemodel_game_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamecolmodel',
            name='big_flush',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='chance',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='field_1',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='field_2',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='field_3',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='field_4',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='field_5',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='field_6',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='four_of_kind',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='full_house',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='general',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='small_flush',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamecolmodel',
            name='three_of_kind',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='game_name',
            field=models.CharField(default='Game 2023-09-02 07:20', max_length=100),
        ),
    ]
