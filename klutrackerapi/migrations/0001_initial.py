# Generated by Django 4.0.2 on 2022-08-19 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('cllg_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(max_length=100)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('no_of_active_backlogs', models.IntegerField()),
                ('crtchoice', models.BooleanField(default=False)),
                ('linkdin', models.CharField(max_length=1000)),
                ('github', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('cllg_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='klutrackerapi.student')),
                ('aws_cp', models.CharField(max_length=250)),
                ('aws_da', models.CharField(max_length=250)),
                ('aws_sa', models.CharField(max_length=250)),
                ('azure_900', models.CharField(max_length=250)),
                ('azure_240', models.CharField(max_length=250)),
                ('google_cloud', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CodingProfile',
            fields=[
                ('cllg_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='klutrackerapi.student')),
                ('codechef_handle', models.CharField(max_length=100)),
                ('codeforces_handle', models.CharField(max_length=100)),
                ('leetcode_handle', models.CharField(max_length=100)),
                ('vjudge_handle', models.CharField(max_length=100)),
            ],
        ),
    ]
