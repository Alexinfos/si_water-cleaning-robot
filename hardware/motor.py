TAG = "[hardware.motor] > "

def checkImport():
    print(TAG + "sucessfully imported !")

# Main functions

# > Button state class
class Buttons:
    fwd = 0
    bwd = 0
    left = 0
    right = 0
    stop = False

# init
buttonState = Buttons()

def fwd():
    if buttonState.fwd != 5 and buttonState.bwd == 0:
        buttonState.fwd += 1
    elif buttonState.bwd != 0:
        buttonState.bwd -= 1
    
    return buttonState

def bwd():
    if buttonState.bwd != 5 and buttonState.fwd == 0:
        buttonState.bwd += 1
    elif buttonState.fwd != 0:
        buttonState.fwd -= 1
    
    return buttonState