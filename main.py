def on_button_b():
    basic.pause(1000)
    basic.show_string("" + str(input.temperature()))
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
        . . . # .
        # . # . .
        . # . . .
        . . . . .
        """)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

basic.show_icon(IconNames.ROLLERSKATE)

def on_forever():
    pass
basic.forever(on_forever)
