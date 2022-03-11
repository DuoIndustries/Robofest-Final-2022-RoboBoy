#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class Robot:

    def __init__(self, yRailMotor, xRailMotor, lDriveMotor, rDriveMotor, driveColor, ultraSensorDrive, ballColor, ultraSensorColor):
        try:

            self.count_balls = 0

            if yRailMotor == 'A':
            self.yRailMotor = Motor(Port.A)
            elif yRailMotor == 'B':
                self.yRailMotor = Motor(Port.B)
            elif yRailMotor == 'C':
                self.yRailMotor = Motor(Port.C)
            elif yRailMotor == 'D':
                self.yRailMotor = Motor(Port.D)
            else:
                print("Error with yRailMotor")
                exit(0)

            if xRailMotor == 'A':
                self.xRailMotor = Motor(Port.A)
            elif xRailMotor == 'B':
                self.xRailMotor = Motor(Port.B)
            elif xRailMotor == 'C':
                self.xRailMotor = Motor(Port.C)
            elif xRailMotor == 'D':
                self.xRailMotor = Motor(Port.D)
            else:
                print("Error with xRailMotor")
                exit(0)

            if lDriveMotor == 'A':
                self.lDriveMotor = Motor(Port.A)
            elif lDriveMotor == 'B':
                self.lDriveMotor = Motor(Port.B)
            elif lDriveMotor == 'C':
                self.lDriveMotor = Motor(Port.C)
            elif lDriveMotor == 'D':
                self.lDriveMotor = Motor(Port.D)
            else:
                print("Error with lDriveMotor")
                exit(0)

            if rDriveMotor == 'A':
                self.rDriveMotor = Motor(Port.A)
            elif rDriveMotor == 'B':
                self.rDriveMotor = Motor(Port.B)
            elif rDriveMotor == 'C':
                self.rDriveMotor = Motor(Port.C)
            elif rDriveMotor == 'D':
                self.rDriveMotor = Motor(Port.D)
            else:
                print("Error with rDriveMotor")
                exit(0)

            if driveColor == '1':
                self.driveColor = ColorSensor(1)
            elif driveColor == '2':
                self.driveColor = ColorSensor(2)
            elif driveColor == '3':
                self.driveColor = ColorSensor(3)
            elif driveColor == '4':
                self.driveColor = ColorSensor(4)
            else:
                print("Error with driveColor")
                exit(0)

            if ultraSensorDrive == '1':
                self.ultraSensorDrive = UltrasonicSensor(1)
            elif ultraSensorDrive == '2':
                self.ultraSensorDrive = UltrasonicSensor(2)
            elif ultraSensorDrive == '3':
                self.ultraSensorDrive = UltrasonicSensor(3)
            elif ultraSensorDrive == '4':
                self.ultraSensorDrive = UltrasonicSensor(4)
            else:
                print("Error with ultraSensorDrive")
                exit(0)
            
            if ballColor == '1':
                self.ballColor = ColorSensor(1)
            elif ballColor == '2':
                self.ballColor = ColorSensor(2)
            elif ballColor == '3':
                self.ballColor = ColorSensor(3)
            elif ballColor == '4':
                self.ballColor = ColorSensor(4)
            else:
                print("Error with ballColor")
                exit(0)

            if ultraSensorColor == '1':
                self.ultraSensorColor = UltrasonicSensor(1)
            elif UltrasonicSensor == '2':
                self.ultraSensorColor = UltrasonicSensor(2)
            elif UltrasonicSensor == '3':
                self.ultraSensorColor = UltrasonicSensor(3)
            elif UltrasonicSensor == '4':
                self.ultraSensorColor = UltrasonicSensor(4)
            else:
                print("Error with ultraSensorColor")
                exit(0)

            print("Settings. Ok!")
        except:
            print("Error. Check all Ports.")
            exit(0)
    
    def driveAlongLine(self, right=True, dist, speed):

        if right:
            while (ultraSensorDrive.distance() > dist):
                if (driveColor.color() == Color.BLACK):
                    lDriveMotor.run(speed - 5)
                    rDriveMotor.run(speed)
                else:
                    lDriveMotor.run(speed)
                    rDriveMotor.run(speed - 5)
        else:
            while (ultraSensorDrive.distance() > dist):
                if (driveColor.color() == Color.BLACK):
                    lDriveMotor.run(speed)
                    rDriveMotor.run(speed - 5)
                else:
                    lDriveMotor.run(speed - 5)
                    rDriveMotor.run(speed)

        lDriveMotor.brake()
        rDriveMotor.brake()
    
    def moveRail(self, pos):

        if (pos == 'takeSecondBall'):
            if self.count_balls == 0:
                xRailMotor.run_angle(20, 100)
                yRailMotor.run_angle(50, 50)
                xRailMotor.run_angle(20, -100)
                yRailMotor.run_angle(50, -50)
            elif self.count_balls == 1:
                xRailMotor.run_angle(20, 200)
                yRailMotor.run_angle(50, 50)
                xRailMotor.run_angle(20, -100)
                yRailMotor.run_angle(50, -50)


def main():
    settings = {'yRailMotor': 'A', 'xRailMotor': 'B', 'lDriveMotor': 'C', 'rDriveMotor': 'D', 'driveColor': '1', 'ultraSensorDrive': '2', 'ballColor': '3', 'ultraSensorColor': '4'}
    robot = Robot(settings['yRailMotor'], settings['xRailMotor'], settings['lDriveMotor'], settings['rDriveMotor'], settings['driveColor'], settings['ultraSensorDrive'], settings['ballColor'], settings['ultraSensorColor'])

if __name__ == "__main__":
    main()