
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa



def render_to_pdf(template_src, context_dict={}):#context_dict is the data we want to pass into the template
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')

	return None


#Automaticly downloads to PDF file
class downloadPortfolio(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('resume/pdf.html')#last params should to data that i have to render to the particular page but in template  i directly give static link in the 

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "NirmalPortfolio.pdf"
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response




#Opens up page as PDF(use this if you want to view page)

class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		# pdf = render_to_pdf('resume/pdf.html', data)
		pdf = render_to_pdf('resume/pdf.html')
		return HttpResponse(pdf, content_type='application/pdf')





def home(request):
    return render(request,'resume/home.html')



from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def sendEmail(request):
    
	if request.method == 'POST':

		template = render_to_string('resume/email_msg.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['nirmalpandey27450112@gmail.com']
			)

		email.fail_silently=False
  
		email.send()

	return render(request, 'resume/email_sent.html')