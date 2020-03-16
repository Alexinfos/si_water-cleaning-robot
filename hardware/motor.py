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
    stop = True

class Motor:
    speed = 0

# init
buttonState = Buttons()
leftMotor = Motor()
rightMotor = Motor()

# Update the buttonstate when a button is pressed
def fwd():
    buttonState.stop = False
    if buttonState.fwd != 5 and buttonState.bwd == 0:
        buttonState.fwd += 1
    elif buttonState.bwd != 0:
        buttonState.bwd -= 1
    
    updateMotor()
    return buttonState

def bwd():
    buttonState.stop = False
    if buttonState.bwd != 5 and buttonState.fwd == 0:
        buttonState.bwd += 1
    elif buttonState.fwd != 0:
        buttonState.fwd -= 1
    
    updateMotor()
    return buttonState

def left():
    buttonState.stop = False
    if buttonState.left != 5 and buttonState.right == 0:
        buttonState.left += 1
    elif buttonState.right != 0:
        buttonState.right -= 1
    
    updateMotor()
    return buttonState

def right():
    buttonState.stop = False
    if buttonState.right != 5 and buttonState.left == 0:
        buttonState.right += 1
    elif buttonState.left != 0:
        buttonState.left -= 1
    
    updateMotor()
    return buttonState

def stop():
    buttonState.right = 0
    buttonState.left = 0
    buttonState.fwd = 0
    buttonState.bwd = 0
    buttonState.stop = True
    
    updateMotor()
    return buttonState

# Get the current status
def getStatus():
    return buttonState

# Calculate the motors speed according to the action asked by the user
def updateMotor():
    if not buttonState.stop:
        leftMotor = rightMotor = (buttonState.fwd * 128/5) - (buttonState.bwd * 127/5)
        
        # TODO: Calculer la vitesse des moteurs lors d'un virage
        #if buttonState.left != 0:
        #    leftMotor = 
        #elif buttonState.right != 0:
        #    rightMotor = 
    else:
        leftMotor = 0
        rightMotor = 0
    
    print(TAG + "leftMotor = " + leftMotor + "; rightMotor = " + rightMotor)