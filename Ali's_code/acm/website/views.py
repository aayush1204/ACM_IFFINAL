from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
	return render(request,'website/home.html')

def team(request):
	return render(request,'website/team.html')

def events(request):
	return render(request,'website/events.html')

def djascii(request):
	return render(request,'website/djascii.html')

def loc(request):
	return render(request,'website/index.html')

def contact(request):
	sent=False
	if request.method == 'POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		message=request.POST.get('message')
		e_mail = EmailMessage(subject,message, 'aakanadia@gmail.com', ['aakanadia@gmail.com'])
		e_mail.send()
		sent=True
	return render(request,'website/contact.html', {'sent':sent})
