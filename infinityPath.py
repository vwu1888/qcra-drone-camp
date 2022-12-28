from easytello import tello

drone = tello.Tello()

midPoint = [1, 1]
apex = [0, 2]


# TODO: Test if this works on a drone
#       Unsure if the coordinates are relative to
#       the drone or the starting position
def infinity(scale=1, height=3, speed=2):
    drone.takeoff()
    if drone.get_height != height:
        drone.up(height - drone.get_height)

    scaledMidPoint = [midPoint[0] * scale, midPoint[1] * scale]
    scaledApex = [apex[0] * scale, apex[1] * scale]

    drone.curve(
        scaledMidPoint[0], scaledMidPoint[1], height, 
        scaledApex[0], scaledApex[1], height, 
        speed=speed)
    drone.curve(
        -scaledMidPoint[0], scaledMidPoint[1], height, 
        scaledMidPoint[0], -scaledMidPoint[1], height, 
        speed=speed)
    drone.curve(
        scaledApex[0], -scaledApex[1], height, 
        -scaledMidPoint[0], -scaledMidPoint[1], height, 
        speed=speed)
    drone.go(0, 0, height, speed=speed)