from machine import Pin,PWM

TAG = "[hardware.io] > "

def checkImport():
    print(TAG + "sucessfully imported !")

# Main functions

# > Integrated LED control
class Led:
    brightness = 0
    pin = None
    pwmController = None
    isOn = False

    def __init__(self, ledPin):
        self.pin = Pin(ledPin, Pin.OUT)
        self.pwmController = PWM(self.pin)
        self.pwmController.freq(500)
    
    def setBrightness(self, newBrightness):
        self.brightness = newBrightness
        if self.isOn:
            self.pwmController.duty(self.brightness)
    
    def off(self):
        self.isOn = False
        self.pwmController.duty(0)

    def on(self):
        self.isOn = True
        self.pwmController.duty(self.brightness)