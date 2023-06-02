from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def load_property():
    properties = [
        {
            "name" : "Jesse's PentHouse",
            "img_url" : "https://images.unsplash.com/photo-1613490493576-7fde63acd811?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDN8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=500&q=60",
        },
       
    {
           "name" : "Light House",
            "img_url" : "https://images.unsplash.com/photo-1597211833712-5e41faa202ea?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fHZpbGxhfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
           
        },
        {
           "name" : "Super Villa",
            "img_url" : "https://images.unsplash.com/photo-1602343168117-bb8ffe3e2e9f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8dmlsbGF8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
           
        }
    ]
    return properties

def load_locations():
    locations = ['Kenya','Tanzania','Ethiopia','Uganda']
    return locations


def load_cities():
    cities = ['Nairobi','Arusha','Addis-Ababa','Kampala']
    return cities

def index(request):
    prop = load_property()
    print(f"PROPERTY: {prop}")
    context = {
        "properties": load_property(),
        "locations": load_locations(),
        "cities": load_cities()
    }
    return render(request, "customer/index.html",context)

def house(request):
    return render(request, "customer/houses.html")

def properties(request):
    return render(request, "customer/properties.html")
    
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