from django.urls import path

from resume_app import views




app_name = 'resume_app'

urlpatterns = [
    path('',views.home,name ="home"),
    path('pdf_download/',views.downloadPortfolio.as_view(),name="pdf_download"),
    path('sent_email/',views.sendEmail,name="sent_email")
 
]
