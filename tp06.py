aprinde = 0
numero = 0

def on_gesture_shake():
    if aprinde == 1:
        for i in range(5):
            for j in range(5):
                led.plot(i, j)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global numero, aprinde
    if input.button_is_pressed(Button.A):
        basic.show_number(input.temperature())
        if input.temperature() > 10 and input.temperature() < 18:
            basic.show_string("Watering the plant")
    if input.button_is_pressed(Button.B):
        numero = randint(0, 100)
        basic.show_number(numero)
        if numero < 60:
            basic.show_string("Watering the plant")
        if numero > 70:
            basic.show_string("Stopped watering the plant")
    if input.logo_is_pressed():
        aprinde = 0
        if input.light_level() > 120:
            aprinde += 1
        if input.light_level() < 120:
            basic.show_string("Stopped watering the plant")
basic.forever(on_forever)
