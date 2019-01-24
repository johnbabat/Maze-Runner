#To be able to test that the robot's motion functionality after build before the code for automation
#Note: GPIO setmode was used here and not BCM

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
import sys, tty, termios, time


try:
        list1 = [3, 5, 7, 11, 13]
        GPIO.setup(15, GPIO.IN)
        for i in list1:
                GPIO.setup(i, GPIO.OUT)

        def move_forward():
                GPIO.output(7, True)
                GPIO.output(3, True)
                GPIO.output(11, True)
                GPIO.output(5, False)
                GPIO.output(13, False)
                

        def move_backward():
                GPIO.output(7, True)
                GPIO.output(5, True)
                GPIO.output(13, True)
                GPIO.output(3, False)
                GPIO.output(11, False)
                

        def move_left():
                GPIO.output(7, True)
                GPIO.output(3, True)
                GPIO.output(13, True)
                GPIO.output(5, False)
                GPIO.output(11, False)
                

        def move_right():
                GPIO.output(7, True)
                GPIO.output(5, True)
                GPIO.output(11, True)
                GPIO.output(3, False)
                GPIO.output(13, False)
                

        def stop():
                GPIO.output(7, False)


        def getch():    #getch function is used to allow the pi recognize input from your keyboard as direct instructions
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                        tty.setraw(sys.stdin.fileno())
                        ch = sys.stdin.read(1)
                finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch



        print("Forward is w, Backward is s, Left is a, Right is d, Stop is x")


        while True:

                char = getch()

                if (char == "w"):       #Takes input as w and maps it to forward movement
                        move_forward()

                elif (char == "s"):     #Takes input as s and maps it to backward movement
                        move_backward()

                elif (char == "a"):     #Takes input as a and maps it to left movement
                        move_left()

                elif (char == "d"):     #Takes input as d and maps it to right movement
                        move_right()

                elif (char == "x"):     #Takes input as x and maps it to stop motion
                        stop()

#To allow you stop the code running by using a keyboard interrupt(Ctrl + C)
        GPIO.cleanup()
except KeyboardInterrupt:
        print(dir_list, i)
        dir_list = []
        GPIO.cleanup()
