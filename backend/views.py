from django.http import HttpResponse
from backend.models import City, Itinerary
from backend.serializers import CitySerializer
from rest_framework import viewsets

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm 

from django.http import JsonResponse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt


from .serializers import CitySerializer,  ItinerarySerializer
from .models import City, Itinerary, Planning


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()

    def get_serializer_class(self):
        return CitySerializer

    def list(self, request, *args, **kwargs):
        movies = City.objects.all()
        serializer = CitySerializer(movies, many=True)
        return Response(serializer.data)
    

class ItineraryViewSet(viewsets.ModelViewSet):

    queryset = Itinerary.objects.all()

    def get_serializer_class(self):
        return ItinerarySerializer

    def list(self, request, *args, **kwargs):
        movies = Itinerary.objects.all()
        serializer = ItinerarySerializer(movies, many=True)
        return Response(serializer.data)
    

# function to call Home Screen
def home_screen(request):
    city_table = City.objects.all()
    # return response 
    return render(request, "t1.html", {"cities": city_table}) 


# function to call City Screen
def city_screen(request): 
    
    # return response 
    city_table = City.objects.all()
    return render(request, "room.html", {"cities": city_table})


# function to call Room Screen
def room_screen(request):
    # return response 
    return render(request, "room.html", {})


def button(request):
   city_table = City.objects.all()
   return render(request, "room.html", {"cities": city_table})


def check(request):
    city_id = request.POST['city_name']
    city_start_date = request.POST['city_start_date']
    city_end_date = request.POST['city_end_date']

    start_date = datetime.strptime(city_start_date, '%Y-%m-%d')
    end_date = datetime.strptime(city_start_date, '%Y-%m-%d')

    city_start_date = [int(date) for date in city_start_date.split("-")]
    city_end_date = [int(date) for date in city_end_date.split("-")]


    # datetime(year, month, day, hour, minute, second)
    end = datetime(city_end_date[0], city_end_date[1], city_end_date[2] + 1, 0, 0, 0)
    start = datetime(city_start_date[0], city_start_date[1], city_start_date[2], 0, 0, 0)
    
    # returns a timedelta object
    delta = end - start 
    date_list = [start + timedelta(days = x) for x in range(delta.days)]

    itinerary = Itinerary.objects.filter(city = city_id, start_day__lte = start, end_day__gte = end).order_by("start_day")

    response = []
    
    if len(itinerary) == 0:

        city = City.objects.get(id = city_id)

        new_itinerary = Itinerary.objects.create(city = city, start_day = start ,  end_day = end, peoples= 2)

        for date in date_list:
            planning = Planning.objects.create(itinerary = new_itinerary, day = date, activity = "")
            response.append({"id": planning.id, "day": planning.day, "activity": planning.activity})

    else:

        previous_itinerary = Itinerary.objects.get(city = city_id)
        planning = Planning.objects.filter(itinerary = previous_itinerary.id)

        if start.date() < itinerary[0].start_day:
            start_delta = itinerary[0].start_day - start.date()
            start_date_list = [start.date() + timedelta(days = x) for x in range(start_delta.days)]

            for date in start_date_list:
                new_planning = Planning.objects.create(itinerary = previous_itinerary, day = date, activity = "")
                response.append({"id": new_planning.id, "day": new_planning.day, "activity": new_planning.activity})


        for plan in planning:
            response.append({"id": plan.id, "day": plan.day, "activity": plan.activity})

        if end.date() > itinerary[len(itinerary) - 1].end_day:
            end_delta = end.date() - itinerary[len(itinerary) - 1].end_day
            end_date_list = [end.date() + timedelta(days = x) for x in range(end_delta.days)]

            for date in end_date_list:
                planning = Planning.objects.create(itinerary = previous_itinerary, day = date, activity = "")
                response.append({"id": planning.id, "day": planning.day, "activity": planning.activity})

    return render(request, "room.html", {"itinerary": response})

def delete_row(request, row_id):
    # Your delete logic goes here
    # For example, remove the row from the database

    print("yeah")

    # Return a JSON response indicating success
    return JsonResponse({'status': 'Row deleted successfully'})


@csrf_exempt
def delete_row(request, row_id):
    # Your delete logic goes here
    # For example, remove the row from the database

    print(row_id)

    planning = Planning.objects.get(id=row_id)
    planning.delete()

    # Return a JSON response indicating success
    return JsonResponse({'status': 'Row deleted successfully'})


@csrf_exempt
def update_row(request, row_id, activity):
    # Your delete logic goes here
    # For example, remove the row from the database

    print(row_id)
    print(activity)


    planning = Planning.objects.get(id=row_id)
    planning.activity = activity
    planning.save()
    
    # Return a JSON response indicating success
    return JsonResponse({'status': 'Row deleted successfully'})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request, 'submit_review.html', {'form': form})

def send_email(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email', '')
        subject = 'booking details'
        message = 'tour coordinator'
        from_email = 'moressanika18@gmail.com'
        recipient_list = [recipient_email]

        send_mail(subject, message, from_email, recipient_list)

        return HttpResponse(f'Email sent successfully to {recipient_email}!')

    return render(request, 'send_email.html')

def Kashmirtrip(request):
    return render(request, 'Kashmirtrip.html')

def Kashmirtrip1(request):
    return render(request, 'kashmirtrip1.html')

def Rome(request):
    return render(request, 'Rome1.html')

def Rometrip(request):
    return render(request, 'rometrip.html')

def Paris(request):
    return render(request, 'paris.html')

def Paristrip(request):
    return render(request, 'paristrip.html')

def Paristrip1(request):
    return render(request, 'paristrip1.html')

def Kashmir(request):
    return render(request, 'KASHMIR.html')