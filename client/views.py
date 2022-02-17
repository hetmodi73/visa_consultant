from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,ListView,DetailView
from .models import user,document,service,service_detail,master_question,sub_question,feedback,contact,crs

# Create your views here.
@login_required

def index(request):
    return render(request, "client/index.html")

def about(request):
    return render(request,"client/about.html")

def contact(request):
    return render(request,"client/contact.html")

def gallery(request):
    return render(request,"client/gallery.html")

def services(request):
    return render(request,"client/services.html")

def typography(request):
    return render(request,"client/typography.html")

def crs_visa_consultant(request):
    return render(request,"client/crs_visa_consultant.html")

def list_user_visa_consultant(request):
    return render(request,"client/list_user_visa_consultant.html")

def list_document_visa_consultant(request):
    return render(request,"client/list_document_visa_consultant.html")

def list_service_visa_consultant(request):
    return render(request,"client/list_service_visa_consultant.html")

def list_service_detail_visa_consultant(request):
    return render(request,"client/list_service_detail_visa_consultant.html")

def list_sub_question_visa_consultant(request):
    return render(request,"client/list_sub_question_visa_consultant.html")

def list_master_question_visa_consultant(request):
    return render(request,"client/list_master_question_visa_consultant.html")

def list_feedback_visa_consultant(request):
    return render(request,"client/list_feedback_visa_consultant.html")

def list_contact_visa_consultant(request):
    return render(request,"client/list_contact_visa_consultant.html")

def list_crs_visa_consultant(request):
    return render(request,"client/list_crs_visa_consultant.html")

class NewUserView(CreateView):
    model = user
    fields = '__all__'
    template_name = 'client/index.html'
    success_url = 'client/list_user_visa_consultant.html'

class ListUserView(ListView):
    model = user
    context_object_name = 'client'
    template_name = 'client/list_user_visa_consultant.html'

class NewDocumentView(CreateView):
    model = document
    fields = '__all__'
    template_name = 'client/services.html'
    success_url = 'client/list_document_visa_consultant.html'

class ListDocumentView(ListView):
    model = document
    context_object_name = 'client'
    template_name = 'client/list_document_visa_consultant.html'

class NewServiceView(CreateView):
    model = service
    fields = '__all__'
    template_name = 'client/services.html'
    success_url = 'client/list_service_visa_consultant.html'

class ListServiceView(ListView):
    model = service
    context_object_name = 'client'
    template_name = 'client/list_service_visa_consultant.html'

class NewService_detailView(CreateView):
    model = service_detail
    fields = '__all__'
    template_name = 'client/services.html'
    success_url = 'client/list_service_detail_visa_consultant.html'

class ListService_detailView(ListView):
    model = service_detail
    context_object_name = 'client'
    template_name = 'client/list_user_visa_consultant.html'

class NewMaster_questionView(CreateView):
    model = master_question
    fields = '__all__'
    template_name = 'client/services.html'
    success_url = 'client/list_master_question_visa_consultant.html'

class ListMaster_questionView(ListView):
    model = master_question
    context_object_name = 'client'
    template_name = 'client/list_master_question_visa_consultant.html'

class NewSub_questionView(CreateView):
    model = sub_question
    fields = '__all__'
    template_name = 'client/services.html'
    success_url = 'client/list_sub_question_visa_consultant.html'

class ListSub_questionView(ListView):
    model = sub_question
    context_object_name = 'client'
    template_name = 'client/list_sub_question_visa_consultant.html'

class NewFeedbackView(CreateView):
    model = feedback
    fields = '__all__'
    template_name = 'client/contact.html'
    success_url = 'client/list_feedback_visa_consultant.html'

class ListFeedbackView(ListView):
    model = feedback
    context_object_name = 'client'
    template_name = 'client/list_feedback_visa_consultant.html'

class NewContactView(CreateView):
    model = contact
    fields = '__all__'
    template_name = 'client/contact.html'
    success_url = 'client/list_contact_visa_consultant.html'

class ListContactView(ListView):
    model = contact
    context_object_name = 'client'
    template_name = 'client/list_contact_visa_consultant.html'

class NewCrsView(CreateView):
    model = crs
    fields = '__all__'
    # template_name = 'client/crs_visa_consultant.html'
    # success_url = 'client/list_crs_visa_consultant.html'

class ListCrsView(ListView):
    model = crs
    context_object_name = 'client'
    template_name = 'client/list_crs_visa_consultant.html'

class DetailCrsView(DetailView):
    model = crs
    success_url = 'client/list_crs_visa_consultant.html'


from django.contrib import messages

def checklogin(request, login=None):
    if request.method == 'POST':

        # Authentication Form

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = login.objects.get(username=username, password=password)
            request.session['log_user'] = user.username
            request.session['log_id'] = user.id
            request.session.save()

        except login.DoesNotExist:
            user = None

        if user is not None:
            return render(request, 'admin')

        else:
            messages.info(request, 'Account does not exits, please Sign in')
    return render(request,'client/login.html')

def viewdata(request):
    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")

        logindata = login(username=username,password=password)
        logindata.save()
        messages.success(request, 'Data has been submitted')
        context = {

            'username': username,
            'password': password
        }

    else:

        context = {'type': 'no data'}

    return render(request, 'client/login.html', context)

def viewdata(request):
    if request.method == 'POST':

        EMAIL_ID = request.POST.get("EMAIL_ID")
        PHONE_NO = request.POST.get("PHONE_NO")
        PASSWORD = request.POST.get("PASSWORD")
        NAME = request.POST.get("NAME")
        GENDER = request.POST.get("GENDER")
        ADDRESS = request.POST.get("ADDRESS")
        ROLE = request.POST.get("ROLE")
        STATUS = request.POST.get("STATUS")

        userdata = user(EMAIL_ID=EMAIL_ID,PHONE_NO=PHONE_NO,PASSWORD='PASSWORD',NAME=NAME,GENDER=GENDER,ADDRESS=ADDRESS,ROLE=ROLE,STATUS=STATUS)
        userdata.save()
        messages.success(request, 'Data has been submitted')
        context = {

            'EMAIL_ID': EMAIL_ID,
            'PHONE_NO': PHONE_NO,
            'PASSWORD': PASSWORD,
            'NAME': NAME,
            'GENDER': GENDER,
            'ADDRESS': ADDRESS,
            'ROLE': ROLE,
            'STATUS': STATUS

        }

    else:

        context = {'type': 'no data'}

    return render(request, 'client/index.html', context)

def viewdata(request):
    if request.method == 'POST':

        L_ID = request.POST.get("L_ID")
        DOCUMENT_NAME = request.POST.get("DOCUMENT_NAME")
        DOCUMENT_FILE = request.POST.get("DOCUMENT_FILE")
        SERVICE_ID = request.POST.get("SERVICE_ID")

        documentdata = user(L_ID=L_ID,DOCUMENT_NAME=DOCUMENT_NAME,DOCUMENT_FILE=DOCUMENT_FILE,SERVICE_ID=SERVICE_ID)
        documentdata.save()
        messages.success(request, 'Data has been submitted')
        context = {

            'L_ID': L_ID,
            'DOCUMENT_NAME': DOCUMENT_NAME,
            'DOCUMENT_FILE': DOCUMENT_FILE,
            'SERVICE_ID': SERVICE_ID,

        }

    else:

        context = {'type': 'no data'}

    return render(request, 'client/services.html', context)

def viewdata(request):
    if request.method == 'POST':

        SERVICE_NAME = request.POST.get("SERVICE_NAME")

        servicedata = user(SERVICE_NAME=SERVICE_NAME)
        servicedata.save()
        messages.success(request, 'Data has been submitted')
        context = {

            'SERVICE_NAME': SERVICE_NAME,

        }

    else:

        context = {'type': 'no data'}

    return render(request, 'client/services.html', context)

def viewdata(request):
    if request.method == 'POST':

        SERVICE_ID = request.POST.get("SERVICE_ID")
        SERVICE_DETAIL_NAME = request.POST.get("SERVICE_DETAIL_NAME")

        service_detaildata = user(SERVICE_ID=SERVICE_ID,SERVICE_DETAIL_NAME=SERVICE_DETAIL_NAME)
        service_detaildata.save()
        messages.success(request, 'Data has been submitted')
        context = {

            'SERVICE_ID': SERVICE_ID,
            'SERVICE_DETAIL_NAME': SERVICE_DETAIL_NAME,

        }

    else:

        context = {'type': 'no data'}

    return render(request, 'client/services.html', context)

def viewdata(request):
    if request.method == 'POST':

        QUESTION = request.POST.get("QUESTION")
        ANSWER = request.POST.get("ANSWER")
        POINTS = request.POST.get("POINTS")
        SD_ID = request.POST.get("SD_ID")

        master_questiondata = user(QUESTION=QUESTION,ANSWER=ANSWER,POINTS=POINTS,SD_ID=SD_ID)
        master_questiondata.save()
        messages.success(request, 'Data has been submitted')
        context = {

            'QUESTION': QUESTION,
            'ANSWER': ANSWER,
            'POINTS': POINTS,
            'SD_ID': SD_ID,

        }

    else:

        context = {'type': 'no data'}

    return render(request, 'client/services.html', context)

def viewdata(request):
    if request.method == 'POST':

        QUESTION_ID = request.POST.get("QUESTION_ID")
        QUESTION = request.POST.get("QUESTION")
        ANSWER = request.POST.get("ANSWER")
        POINTS = request.POST.get("POINTS")
        SD_ID = request.POST.get("SD_ID")

        sub_questiondata = user(QUESTION_ID=QUESTION_ID,QUESTION=QUESTION,ANSWER=ANSWER,POINTS=POINTS,SD_ID=SD_ID)
        sub_questiondata.save()
        messages.success(request, 'Data has been submitted')
        context = {

            'QUESTION_ID': QUESTION_ID,
            'QUESTION': QUESTION,
            'ANSWER': ANSWER,
            'POINTS': POINTS,
            'SD_ID': SD_ID,

        }

    else:

        context = {'type': 'no data'}

    return render(request, 'client/services.html', context)

def viewdata(request):
    if request.method == 'POST':

        L_ID = request.POST.get("L_ID")
        RATINGS = request.POST.get("RATINGS")
        COMMENT = request.POST.get("COMMENT")

        feedbackdata = user(L_ID=L_ID,RATINGS=RATINGS,COMMENT=COMMENT)
        feedbackdata.save()
        messages.success(request, 'Data has been submitted')
        context = {

            'L_ID': L_ID,
            'RATINGS': RATINGS,
            'COMMENT': COMMENT,

        }

    else:

        context = {'type': 'no data'}

    return render(request, 'client/contact.html', context)

def viewdata(request):
    if request.method == 'POST':

        NAME = request.POST.get("NAME")
        EMAIL = request.POST.get("EMAIL")
        NUMBER = request.POST.get("NUMBER")
        MESSAGE = request.POST.get("MESSAGE")

        sub_questiondata = user(NAME=NAME,EMAIL=EMAIL,NUMBER=NUMBER,MESSAGE=MESSAGE)
        sub_questiondata.save()
        messages.success(request, 'Data has been submitted')
        context = {

            'NAME': NAME,
            'EMAIL': EMAIL,
            'NUMBER': NUMBER,
            'MESSAGE': MESSAGE,

        }

    else:

        context = {'type': 'no data'}

    return render(request, 'client/contact.html', context)
