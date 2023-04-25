from django.shortcuts import render, redirect
from .models import HomeName, HomeImage, Contact, About
# Create your views here.

def home(request):
    home_name = HomeName.objects.all()[0]
    home_image = HomeImage.objects.all()
    return render(request, 'main/home.html', context={
       'home_name':home_name ,
       'home_image':home_image
    })

def about(request):
    about_info = About.objects.all()[0]
    return render(request, 'main/about.html', context={'about_info':about_info})


def contact(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        review = request.POST.get('review')
        Contact.objects.create(username=username, email=email, review=review)
        return redirect('home')

    return render(request, 'main/contact.html')


def review(request):
    review_list = Contact.objects.all()
    return render(request, 'main/review.html', context={
        'review_list':review_list
    })