from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
        if request.method == "POST":
                car_id = request.POST['car_id']
                car_year = request.POST['car_year']
                car_title = request.POST['car_title']
                car_model = request.POST['car_model']
                user_id = request.POST['user_id']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                customer_need = request.POST['customer_need']
                city = request.POST['city']
                state = request.POST['state']
                email = request.POST['email']
                phone = request.POST['phone']
                message = request.POST['message']
                
                if request.user.is_authenticated:
                        user_id = request.user.id
                        has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
               
                        if has_contacted:
                                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                
                                return redirect('/cars/'+car_id)
                
                contact = Contact(car_id=car_id, car_year=car_year, car_title=car_title, car_model=car_model, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)
                
                admin_info=User.objects.get(is_superuser=True)
                admin_email = admin_info.email
                
                send_mail(
                        'New Car Inquiry', #subject
                        'You have a new inquiry for the vehicle ' + car_year + ' ' + car_title + ' ' + car_model + '. Please login to your admin panel for more info. ', #message
                        'canadiancommunism99@gmail.com', #from
                        [admin_email],
                        fail_silently=False,
                )
                
                contact.save()
                
                messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
                
                return redirect('/cars/' + car_id)