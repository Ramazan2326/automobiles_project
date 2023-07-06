from .models import Car
from django.forms import ModelForm, TextInput, Textarea


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["car_title", "car_year", "car_mileage", "car_description", "car_price"]
        widgets = {
            "car_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название автомобиля',
            }),
            "car_year": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите год выпуска',
            }),
            "car_mileage": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пробег автомобиля',
            }),
            "car_description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание автомобиля',
            }),
            "car_price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите стоимость автомобиля',
            })
        }