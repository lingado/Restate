from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from .forms import *
# Create your views here.


def dashboard(request):
    return render(request, "staff/dashboard.html")

def houses(request):
    form = HouseForm()

    if request.method == 'POST':
        print(f"DATA:::{request.POST}")
        form= HouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer:index')

    context = {
        'form' : form
    }
    return render(request, "staff/house_form.html", context)

def customer(request):
    form = CustomerForm()

    if request.method == 'POST':
        form= CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer:index')

    context = {
        'form' : form
    }
    return render(request, "staff/customer_form.html", context)

def location(request):
    form = LocationForm()

    if request.method == 'POST':
        form= LocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = LocationForm()

    context = {
        'form' : form,
        'locations': Location.objects.all()
    }
    return render(request, "staff/location_form.html", context)

def housetypes(request):
    form = HouseTypeForm()

    if request.method == 'POST':
        form= HouseTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer:index')

    context = {
        'form' : form,
        'housetypes' : HouseType.objects.all()
    }
    return render(request, "staff/housetype_form.html", context)

def location_houses(request, location_id):
    location = Location.objects.filter(id=location_id).first()
    
    context = {
        
        "location" : location
    }
    return render(request, "staff/location_houses.html", context)

def house_location_details(request, location_id, property_id):
    house = House.objects.get(id=property_id)
    form = HouseForm(instance=house)

    if request.method == "POST":
        print(request.POST)

        if dict(request.POST) != model_to_dict(house):
           form = HouseForm(request.POST, request.FILES, instance=house)
           if form.is_valid:
            form.save()
    context = {
      "house" : house,
      "form" : form
    }
    return render(request, "staff/house_location.html", context)

def messages(request):
    all_messages = Message.objects.filter(is_read=False)

    context = {
        "messages" : all_messages
    }
    return render(request, "staff/messages.html", context)

def message_details(request, message_id):
    message = Message.objects.get(id=message_id)

    context = {
        "message" : message
    }

    return render(request, "staff/message_details.html", context)


