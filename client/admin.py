from django.contrib import admin
from.models import user,document,service,service_detail,master_question,sub_question,feedback,contact

# Register your models here.

class showuser(admin.ModelAdmin):
    list_display = ['EMAIL_ID','PHONE_NO','PASSWORD','NAME','GENDER','ADDRESS','ROLE','STATUS']

admin.site.register(user,showuser)

class showdocument(admin.ModelAdmin):
    list_display = ['L_ID','DOCUMENT_NAME','DOCUMENT_FILE','SERVICE_ID']

admin.site.register(document,showdocument)

class showservice(admin.ModelAdmin):
    list_display = ['SERVICE_NAME']

admin.site.register(service,showservice)

class showservice_detail(admin.ModelAdmin):
    list_display = ['SERVICE_ID','SERVICE_DETAIL_NAME']

admin.site.register(service_detail,showservice_detail)

class showmaster_question(admin.ModelAdmin):
    list_display = ['QUESTION','ANSWER','POINTS','SD_ID']

admin.site.register(master_question,showmaster_question)

class showsub_question(admin.ModelAdmin):
    list_display = ['QUESTION_ID','QUESTION','ANSWER','POINTS','SD_ID']

admin.site.register(sub_question,showsub_question)

class showfeedback(admin.ModelAdmin):
    list_display = ['L_ID','RATINGS','COMMENT']

admin.site.register(feedback,showfeedback)

class showcontact(admin.ModelAdmin):
    list_display = ['NAME','EMAIL','NUMBER','MESSAGE']

admin.site.register(contact,showcontact)
