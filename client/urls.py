from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('index/',index, name='index'),
    path('about/',about,name='about'),
    path('contact/',contact, name='contact'),
    path('typography/',typography, name='typography'),
    path('services/',services, name='services'),
    path('gallery/',gallery, name='gallery'),
    path('crs_visa_consultant/',crs_visa_consultant, name='crs_visa_consultant'),

    path('list_user_visa_consultant/',ListUserView.as_view(),name='user-list_user_visa_consultant'),
    path('list_document_visa_consultant/',ListDocumentView.as_view(),name='document-list_document_visa_consultant'),
    path('list_service_visa_consultant/',ListServiceView.as_view(),name='service-list_service_visa_consultant'),
    path('list_service_detail_visa_consultant',ListService_detailView.as_view(),name='service_detail-list_service_detail_visa_consultant'),
    path('list_sub_question_visa_consultant/',ListSub_questionView.as_view(),name='sub_question-list_sub_question_visa_consultant'),
    path('list_master_question_visa_consultant/',ListMaster_questionView.as_view(),name='master_question-list_master_question_visa_consultant'),
    path('list_feedback_visa_consultant/',ListFeedbackView.as_view(),name='feedback-list_feedback_visa_consultant'),
    path('list_contact_visa_consultant/', ListContactView.as_view(), name='contact-list_contact_visa_consultant'),
    path('list_crs_visa_consultant/',ListCrsView.as_view(),name='crs-list_crs_visa_consultant'),

    path('detail_crs_visa_consultant/',DetailCrsView.as_view(), name="crs-detail_crs_visa_consultant")
]
