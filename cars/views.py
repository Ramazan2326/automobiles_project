from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, StreamingHttpResponse
from .models import Car
from .forms import CarForm
from wsgiref.util import FileWrapper
import csv, mimetypes, os


def index(request):
    cars = Car.objects.all()
    summa = 0
    with open ('file.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(['id', 'Name', 'Mileage', 'Cost'])
        for car in cars:
            summa += int(car.car_price)
            writer.writerow([car.id, car.car_title, car.car_mileage, car.car_price])
        writer.writerow(['Total price:', summa])
    return render(request, 'cars/index.html', {'cars': cars})


def create(request):
    error = ''
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cars')
        else:
            error = 'Форма была неверной'
    form = CarForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'cars/form.html', context)


def edit(request, id):
    try:
        cars = Car.objects.get(id=id)
        if request.method == "POST":
            cars.car_title = request.POST.get('car_title')
            cars.car_price = request.POST.get('car_price')
            cars.car_year = request.POST.get('car_year')
            cars.car_mileage = request.POST.get('car_mileage')
            cars.car_description = request.POST.get('car_description')
            cars.save()
            return redirect("/cars")
        else:
            return render(request, "cars/edit.html", {'car':cars})
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Car not found</h2>")


def edit_page(request):
    cars = Car.objects.all()
    return render(request, 'cars/edit_db.html', {'cars': cars})


def delete(request, id):
    try:
        person = Car.objects.get(id=id)
        person.delete()
        return redirect('/cars')
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Car not found</h2>")


def about(request):
    return render(request, 'cars/about.html')


def contact(request):
    return render(request, 'cars/contacts.html')


def downloadfile(request):
    filename = 'file.csv'
    filepath = 'project/file.csv'
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'), chunk_size), content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;filename=%s"%filename
    return response
