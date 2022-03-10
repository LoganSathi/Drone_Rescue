from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()  # Connects to drone
print(me.get_battery())  # Gets drone battery percentage

me.streamon()  # Turns on camera

while True:
    img = me.get_frame_read().frame  # Get individual image frames from camera
    img = cv2.resize(img, (360, 240))  # Set frame size of image
    cv2.imshow("Image", img)  # Display image
    cv2.waitKey(1)  # Delay before frame displayed shuts down for 1 millisecond
