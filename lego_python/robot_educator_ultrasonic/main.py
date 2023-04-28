#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Ultrasonic Sensor Driving Base Program
-----------------------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

# Komentar od Miroslav Kramar

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Zalozeni kostky
ev3 = EV3Brick()

# Zalozeni ultrazvukoveho senzoru, ktery bude pripojen na port cislo 4
obstacle_sensor = UltrasonicSensor(Port.S4)

# Zalozeni dvou motoru, levy motor bude pripojen na portu B a pravy motor na portu C
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Zalozeni DriveBase. DriveBase bude mit oba dva jiz zalozene motory, prumer kol 55.5 mm a delku hridele 104 mm
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Reproduktor na kostce zapipa
ev3.speaker.beep()

# Program na vyhybani se prekazkam
while True:
    # Robot se rozjede rychlosti 200 mm za sekundu
    robot.drive(200, 0)

    # Robot bude porad cekat 10 milisekund (velmi kratkou dobu :D), dokud bude ultrazvukovy senzor ukazovat vzdalenost vetsi, nez 300 milimetru
    # Jakmile bude vzdalenost kratsi nez 300 milimetru, tak cyklus while skonci a prejde se na dalsi prikazy
    while obstacle_sensor.distance() > 300:
        wait(10)

    # Robot pojede rovne dopredu o -300 milimetru (takze o 300 milimetru dozadu).
    robot.straight(-300)

    # Robot se otoci o 120 stupnu. Vypocet probehne na zaklade parametru predanych DriveBase pri jejim zalozeni
    robot.turn(120)
