from django.shortcuts import render, redirect
from django.core.mail import send_mail
from staff.models import *

# Create your views here.
def load_property():
    properties = House.objects.all().order_by('-id')
    return properties

def load_locations():
    locations = Location.objects.all()
    return locations


def load_cities():
    cities = ['Nairobi','Arusha','Addis-Ababa','Kampala']
    return cities

def index(request):
    latest_properties = load_property()
    context = {
        "properties": latest_properties[:5],
        "locations": load_locations(),
        "cities": load_cities()
    }
    return render(request, "customer/index.html",context)

def house(request):
    return render(request, "customer/houses.html")

def properties(request):
    all_properties = House.objects.all()

    context = {
        "houses" : all_properties
    }

    return render(request, "customer/properties.html", context)
    
def contacts(request):
    return render(request, "customer/contacts.html")
def submit_message(request):
    message = ""
    if request.method == 'POST':
        message_details_dict = request.POST
        print(f"FIRST NAME= {message_details_dict.get('first-name')}")
   
        firstname = message_details_dict.get('first-name')
        lastname = message_details_dict.get('last-name')
        email = message_details_dict.get('email')
        phonenumber = message_details_dict.get('phone-number')
        message = message_details_dict.get('message')

        is_sent= send_email(firstname, lastname,phonenumber,email,message)

        if is_sent:
           message = "Email has been sent successfully"
        else:
            message = "Sorry, your email was not sent"

        context = {
            "is_sent": is_sent,
            "message": message
        }            
        return render(request, "customer/contacts.html", context)

    return redirect('customer:contacts')

def send_email(firstname, lastname, phonenumber, sender_email, body):
    sent_successfully = False
    email_subject = f'Inquiry from {firstname} {lastname}'
    detailed_body = f'{body} \n \nContact {firstname} through the phone number: {phonenumber}'

    try:
        send_mail(
            email_subject,
            detailed_body,
            sender_email,
            ['deslingado@gmail.com'],
            fail_silently=False
                
        )
        sent_successfully = True
    except Exception as e:
        print("Email was not sent")

    return sent_successfully


def property_details(request, property_id):
    property = House.objects.get(id=property_id)

    context = {
        "property": property
    }

    return render(request, "customer/property_details.html", context)

def house_types(request):
    house_type_list = HouseType.objects.all()

    print(f"HOUSE TYPE::: {house_type_list}")

    context = {
        "house_types" : house_type_list
    }

    return render(request, "customer/houses.html", context)


def houses_in_category(request, category_id):
    houses = House.objects.filter(house_type__id=category_id)

    context = {
        "properties" : houses
    }

    return render(request, "customer/houses_in_category.html", context)

def search(request):
    
    
   
