from django.db import models
from django.urls import reverse
# Create your models here.

class user(models.Model):
    # L_ID=models.IntegerField(null=True)
    EMAIL_ID=models.CharField(max_length=25)
    PHONE_NO=models.IntegerField()
    PASSWORD=models.CharField(max_length=25)
    NAME=models.CharField(max_length=25)
    choice1=(
        ('male','male'),
        ('female','female'),
        ('other','other')
    )
    GENDER=models.CharField(max_length=25,choices=choice1)
    ADDRESS=models.TextField(max_length=25)
    ROLE=models.IntegerField()
    STATUS=models.IntegerField()

    def __str__(self):
        return self.NAME

    def get_absolute_url(self):
        return reverse('user-list_user_visa_consultant')

class service(models.Model):
    # SERVICE_ID=models.IntegerField(null=True)
    SERVICE_NAME=models.CharField(max_length=25)

    def __str__(self):
        return self.SERVICE_NAME

    def get_absolute_url(self):
        return reverse('service-list_service_visa_consultant')

class document(models.Model):
    # DOCUMENT_ID=models.IntegerField(null=True)
    L_ID=models.ForeignKey(user,on_delete=models.CASCADE, related_name='document')
    DOCUMENT_NAME=models.CharField(max_length=20)
    DOCUMENT_FILE=models.FileField(default="",upload_to="profile")
    SERVICE_ID=models.ForeignKey(service,on_delete=models.CASCADE, related_name='document')

    def __str__(self):
        return self.L_ID, self.SERVICE_ID

    def get_absolute_url(self):
        return reverse('document-list_document_visa_consultant')

class service_detail(models.Model):
    # SD_ID=models.IntegerField(null=True)
    SERVICE_ID=models.ForeignKey(service,on_delete=models.CASCADE, related_name='service_detail')
    SERVICE_DETAIL_NAME=models.CharField(max_length=25)

    def __str__(self):
        return self.SERVICE_ID

    def get_absolute_url(self):
        return reverse('service_detail-list_service_detail_visa_consultant')

class master_question(models.Model):
    # QUESTION_ID=models.IntegerField(null=True)
    QUESTION=models.CharField(max_length=50)
    ANSWER=models.CharField(max_length=50)
    POINTS=models.IntegerField()
    SD_ID=models.ForeignKey(service_detail,on_delete=models.CASCADE, related_name='master_question')

    def __str__(self):
        return self.SD_ID

    def get_absolute_url(self):
        return reverse('master_question-list_master_question_visa_consultant')

class sub_question(models.Model):
    # SUB_QUESTION_ID=models.IntegerField(null=True)
    QUESTION_ID=models.ForeignKey(master_question,on_delete=models.CASCADE, related_name='sub_question')
    QUESTION=models.CharField(max_length=50)
    ANSWER=models.CharField(max_length=50)
    POINTS=models.IntegerField()
    SD_ID=models.ForeignKey(service_detail,on_delete=models.CASCADE, related_name='sub_question')

    def __str__(self):
        return self.QUESTION_ID, self.SD_ID

    def get_absolute_url(self):
        return reverse('sub_question-list_sub_question_visa_consultant')

class feedback(models.Model):
    # FEED_ID=models.IntegerField(null=True)
    L_ID=models.ForeignKey(user,on_delete=models.CASCADE, related_name='feedback')
    RATINGS=models.CharField(max_length=25)
    COMMENT=models.CharField(max_length=25)

    def __str__(self):
        return self.L_ID

    def get_absolute_url(self):
        return reverse('feedback-list_feedback_visa_consultant')

class contact(models.Model):
    # CONTACT_ID=models.IntegerField(null=True)
    NAME=models.CharField(max_length=25)
    EMAIL=models.CharField(max_length=25)
    NUMBER=models.IntegerField()
    MESSAGE=models.TextField(max_length=25)

    def __str__(self):
        return self.EMAIL

    def get_absolute_url(self):
        return reverse('contact-list_contact_visa_consultant')

class crs(models.Model):
    root_age=models.IntegerField()
    root_education_level=models.CharField(max_length=35)
    choice1=(
        ('true','true'),
        ('false','false')
    )
    root_studied_in_canada=models.CharField(max_length=35, choices=choice1)
    root_english_reading=models.CharField(max_length=35)
    root_english_speaking=models.CharField(max_length=35)
    root_english_listening=models.CharField(max_length=35)
    root_english_writing=models.CharField(max_length=35)
    root_french_reading=models.CharField(max_length=35)
    root_french_speaking=models.CharField(max_length=35)
    root_french_listening=models.CharField(max_length=35)
    root_french_writing=models.CharField(max_length=35)
    root_work_foreign_skilled_work_years=models.CharField(max_length=35)
    root_work_canadian_skilled_work_years=models.CharField(max_length=35)
    choice2=(
        ('true','true'),
        ('false','false')
    )
    root_maratial_status=models.CharField(max_length=35, choices=choice2)
    choice3=(
        ('true','true'),
        ('false','false')
    )
    root_spouse_siblings=models.CharField(max_length=35, choices=choice3)
    choice4=(
        ('true','true'),
        ('false','false')
    )
    root_trades_certificate=models.CharField(max_length=35, choices=choice4)
    choice5=(
        ('true','true'),
        ('false','false')
    )
    root_nomination_certificate=models.CharField(max_length=35, choices=choice5)
    choice6=(
        ('true','true'),
        ('false','false')
    )
    root_skilled_job_offer=models.CharField(max_length=35, choices=choice6)
    root_contact_details_residence_country=models.CharField(max_length=35)
    root_contact_details_name=models.CharField(max_length=35)
    root_contact_details_email=models.EmailField(max_length=35)
    root_contact_details_telephone=models.IntegerField()

    def __str__(self):
        return self.root_age

    def get_absolute_url(self):
        return reverse('crs-list_crs_visa_consultant')

