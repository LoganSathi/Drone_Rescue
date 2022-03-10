from djitellopy import tello
from time import sleep
import cv2

me = tello.Tello()
me.connect()  # Connects to Drone
print(me.get_battery())  # Gets Drone battery percentage

me.streamon()  # Turns on camera
#
# me.takeoff()  # Takes off drone
# me.send_rc_control(0, 50, 0, 0)  # Move forward at speed 50 units
# sleep(2)  # Delay while executing previous code line
# me.send_rc_control(0, 0, 0, 30)  # Rotate right at speed 30 units
# sleep(2)
# me.send_rc_control(0, 0, 0, 0)  # Stop moving
# me.land()  # Land



# while True:
me.takeoff()  # Takes off drone
me.send_rc_control(0, 50, 0, 0)  # Move forward at speed 50 units
sleep(2)  # Delay while executing previous code line
me.send_rc_control(0, 0, 0, 30)  # Rotate right at speed 30 units
sleep(2)
me.send_rc_control(0, 0, 0, 0)  # Stop moving
me.land()  # Land

while me:
    img = me.get_frame_read().frame  # Get individual image frames from camera
    img = cv2.resize(img, (360, 240))  # Set frame size of image
    cv2.imshow("Image", img)  # Display image
    cv2.waitKey(1)  # Delay before frame displayed shuts down for 1 millisecond