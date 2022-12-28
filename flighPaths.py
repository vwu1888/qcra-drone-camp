from easytello import tello

myDrone = tello.Tello()


def squarePath(speed=1):
    myDrone.set_speed = speed
    myDrone.takeoff()

    for _ in range(4):
        myDrone.forward(100)
        myDrone.cw(90)

    myDrone.land()


def circlePath(speed=1):
    myDrone.set_speed = speed
    myDrone.takeoff()

    for _ in range(3):
        myDrone.forward(100)
        myDrone.cw(120)

    myDrone.land()


def combineSquareCircle(speed=1):
    squarePath(speed=speed)
    circlePath(speed=speed)
