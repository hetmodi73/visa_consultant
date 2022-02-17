# Generated by Django 4.0.1 on 2022-02-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_contact_contact_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='crs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_age', models.IntegerField()),
                ('root_education_level', models.CharField(max_length=35)),
                ('root_studied_in_canada', models.CharField(choices=[('true', 'true'), ('false', 'false')], max_length=35)),
                ('root_english_reading', models.CharField(max_length=35)),
                ('root_english_speaking', models.CharField(max_length=35)),
                ('root_english_listening', models.CharField(max_length=35)),
                ('root_english_writing', models.CharField(max_length=35)),
                ('root_french_reading', models.CharField(max_length=35)),
                ('root_french_speaking', models.CharField(max_length=35)),
                ('root_french_listening', models.CharField(max_length=35)),
                ('root_french_writing', models.CharField(max_length=35)),
                ('root_work_foreign_skilled_work_years', models.CharField(max_length=35)),
                ('root_work_canadian_skilled_work_years', models.CharField(max_length=35)),
                ('root_maratial_status', models.CharField(choices=[('true', 'true'), ('false', 'false')], max_length=35)),
                ('root_spouse_siblings', models.CharField(choices=[('true', 'true'), ('false', 'false')], max_length=35)),
                ('root_trades_certificate', models.CharField(choices=[('true', 'true'), ('false', 'false')], max_length=35)),
                ('root_nomination_certificate', models.CharField(choices=[('true', 'true'), ('false', 'false')], max_length=35)),
                ('root_skilled_job_offer', models.CharField(choices=[('true', 'true'), ('false', 'false')], max_length=35)),
                ('root_contact_details_residence_country', models.CharField(max_length=35)),
                ('root_contact_details_name', models.CharField(max_length=35)),
                ('root_contact_details_email', models.EmailField(max_length=35)),
                ('root_contact_details_telephone', models.IntegerField()),
            ],
        ),
    ]
