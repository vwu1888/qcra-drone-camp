from easytello import tello

drone = tello.Tello()


def squarePath(speed=1):
    drone.set_speed = speed
    drone.takeoff()

    for _ in range(4):
        drone.forward(100)
        drone.cw(90)

    drone.land()


def circlePath(speed=1):
    drone.set_speed = speed
    drone.takeoff()

    for _ in range(3):
        drone.forward(100)
        drone.cw(120)

    drone.land()


def combineSquareCircle(speed=1):
    squarePath(speed=speed)
    circlePath(speed=speed)
