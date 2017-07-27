import time

lastTime = time.time()
lastAcc = 0
velocity = 0

# call everytime, acceleration is updated
def updateVelocity(acceleration):
    
    global velocity, lastAcc, lastTime
    
    currentTime = time.time()
    velocity += 0.5 * (lastAcc + acceleration) * (currentTime - lastTime)
    
    lastTime  = currentTime
    lastAcc = acceleration

