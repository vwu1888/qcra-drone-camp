from easytello import tello

myDrone = tello.Tello()


def squarePath():
    myDrone.takeoff()

    for _ in range(4):
        myDrone.forward(100)
        myDrone.cw(90)

    myDrone.land()


def circlePath():
    myDrone.takeoff()

    for _ in range(3):
        myDrone.forward(100)
        myDrone.cw(120)

    myDrone.land()


def combineSquareCircle():
    squarePath()
    circlePath()
