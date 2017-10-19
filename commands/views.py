import time

from django.shortcuts import render
from django.conf import settings

import RPi.GPIO as gpio

# Create your views here.
pins = {
    1: settings.PIN_1,
    2: settings.PIN_2,
    3: settings.PIN_3,
    4: settings.PIN_4,
}

def index(request):
    gpio.setmode(gpio.BOARD)

    pins_status = {}

    gpio.setup(pins.values(), gpio.OUT)
    for key, pin in pins.items():
        pins_status[key] = 'On' if gpio.input(pin) == gpio.HIGH else 'Off'

    render(request, 'index.html', {'pins_status': pins_status})

def test_pin(request, which_pin):
    gpio.output(which_pin, True)

def forward(request):
    pass

def stop(request):
    pass