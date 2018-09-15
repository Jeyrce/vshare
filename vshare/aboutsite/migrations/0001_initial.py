# Generated by Django 2.0.3 on 2018-04-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MsgBoard',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('create_time', models.CharField(max_length=19, verbose_name='留言时间')),
                ('nickname', models.CharField(max_length=10, verbose_name='留言昵称')),
                ('content', models.TextField(verbose_name='内容')),
                ('email', models.CharField(max_length=30, verbose_name='邮箱')),
                ('is_delet', models.IntegerField(default=0, verbose_name='是否已删除')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': '网站留言版',
            },
        ),
        migrations.CreateModel(
            name='TopNotice',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=300, verbose_name='内容')),
                ('create_time', models.CharField(max_length=19, verbose_name='发布时间')),
                ('is_delet', models.IntegerField(default=0, verbose_name='是否已删除')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': '置顶公告',
            },
        ),
        migrations.CreateModel(
            name='VisitDocument',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=20, verbose_name='主机ip')),
                ('visit_time', models.CharField(max_length=19, verbose_name='访问时间')),
                ('is_delet', models.IntegerField(default=0, verbose_name='是否已删除')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': '网站统计',
            },
        ),
    ]
