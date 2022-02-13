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

