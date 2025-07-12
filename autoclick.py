import numpy as np
import pyautogui
import cv2
import time
import keyboard
import PIL

#settings for hunter:
confidence = 0.7 #Change this to change the confidence required for the search to be successful.
timeToWaitBetweenChecks = 1 #1 second, can be fractional. like 0.5  lower values will use more cpu due to more frequent checks.
#Enjoy :3


done = False
print("Hold Q to quit when done :3 ~wunder <3")
button_image = cv2.imread("button_image.png")  # Should be local directory. #Moved up here, only has to be read once.
h, w, _ = button_image.shape #Moved up here, only read once.
while not done: #Loop until user input every 1 second
    time.sleep(timeToWaitBetweenChecks) #This does wait every 1 second, it could possibly run even quicker to shave off time between button presses when they occur but I didn't want to spike cpu usage too much lol. Perhaps it can be changed assuming the library we are using for image recognition is not too heavy.
    if(keyboard.is_pressed("Q") or keyboard.is_pressed("q")):
        done = True #We are done
        break
    screenshot = pyautogui.screenshot()
    #https://coderspacket.com/posts/scan-for-a-image-on-the-screen-using-python/ <- found a site which had listed basically some stuff that we wanted to do. Pog. Internet is a part of coding. We can reinvent the wheel if need be that requires actually reading the documentation for the packages.
    screenshot_np = np.array(screenshot)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(screenshot_np,button_image,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= confidence:
        center_x = max_loc[0] + w // 2 # I assume the max_loc is the left/right most and top/bottom most. Which is why the site recommends adding the length of the image divided by 2 thus giving center.
        center_y = max_loc[1] + h // 2
        pyautogui.leftClick(center_x,center_y)
        print("image found and clicked, Hold Q to quit when done")
        pyautogui.move(-h * 2, -w * 2)  # The shitty mod stuff was checking if mouse in same place not to allow click so we shift it to the left lol.

print("All done! c:")
#edittt?