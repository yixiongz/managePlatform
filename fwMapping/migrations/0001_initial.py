# Generated by Django 2.1.3 on 2019-06-04 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laninter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lanip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapid', models.PositiveIntegerField()),
                ('serid', models.PositiveIntegerField()),
                ('protocol', models.IntegerField(choices=[(1, 'udp'), (2, 'tcp'), (3, 'icmp')], default=1)),
                ('lanport', models.PositiveIntegerField()),
                ('wanport', models.PositiveIntegerField()),
                ('lanip', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fwMapping.Laninter')),
            ],
        ),
        migrations.CreateModel(
            name='Waninter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wanip', models.GenericIPAddressField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='laninter',
            name='wanip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fwMapping.Waninter', to_field='wanip'),
        ),
        migrations.AlterUniqueTogether(
            name='mapping',
            unique_together={('lanip', 'lanport', 'wanport')},
        ),
    ]
