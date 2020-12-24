# Generated by Django 3.1.4 on 2020-12-23 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('parentDepartment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.department')),
            ],
        ),
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('holiday_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('last_active', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10)),
                ('birthday', models.DateField()),
                ('join_date', models.DateField()),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('leave_days', models.IntegerField()),
                ('flag', models.CharField(choices=[('1', 'Enabled'), ('0', 'Disabled')], default='1', max_length=4)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.department')),
                ('roles', models.ManyToManyField(to='application.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_days', models.IntegerField()),
                ('reason', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('approver', models.CharField(max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='supervisor',
            field=models.ForeignKey(blank=True, default='', limit_choices_to={'roles': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supevisor', to='application.user'),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
    ]
