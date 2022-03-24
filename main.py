#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep


def checkColor(color):
    if color != Color.BROWN:
        return color
    else:
        return Color.YELLOW

class Robot:

    def __init__(self, yRailMotor, xRailMotor, lDriveMotor, rDriveMotor, driveColor, ultraSensorDrive, ballColorFront, ballColorBack):
        self.count_balls = 0
        self.bay_colors = [[Color.WHITE, Color.WHITE, Color.WHITE], [Color.WHITE, Color.WHITE, Color.WHITE], [Color.WHITE, Color.WHITE, Color.WHITE]]
        self.que_colors = {}
        self.decomp_que = []

        try:
            if yRailMotor == 'A':
                self.yRailMotor = Motor(Port.A)
            elif yRailMotor == 'B':
                self.yRailMotor = Motor(Port.B)
            elif yRailMotor == 'C':
                self.yRailMotor = Motor(Port.C)
            elif yRailMotor == 'D':
                self.yRailMotor = Motor(Port.D)
        except:
            pass

        try:
            if xRailMotor == 'A':
                self.xRailMotor = Motor(Port.A)
            elif xRailMotor == 'B':
                self.xRailMotor = Motor(Port.B)
            elif xRailMotor == 'C':
                self.xRailMotor = Motor(Port.C)
            elif xRailMotor == 'D':
                self.xRailMotor = Motor(Port.D)
        except:
            pass

        try:
            if lDriveMotor == 'A':
                self.lDriveMotor = Motor(Port.A)
            elif lDriveMotor == 'B':
                self.lDriveMotor = Motor(Port.B)
            elif lDriveMotor == 'C':
                self.lDriveMotor = Motor(Port.C)
            elif lDriveMotor == 'D':
                self.lDriveMotor = Motor(Port.D)
        except:
            pass


        try:
            if rDriveMotor == 'A':
                self.rDriveMotor = Motor(Port.A)
            elif rDriveMotor == 'B':
                self.rDriveMotor = Motor(Port.B)
            elif rDriveMotor == 'C':
                self.rDriveMotor = Motor(Port.C)
            elif rDriveMotor == 'D':
                self.rDriveMotor = Motor(Port.D)
        except:
            pass

        try:
            if driveColor == '1':
                self.driveColor = ColorSensor(Port.S1)
            elif driveColor == '2':
                self.driveColor = ColorSensor(Port.S2)
            elif driveColor == '3':
                self.driveColor = ColorSensor(Port.S3)
            elif driveColor == '4':
                self.driveColor = ColorSensor(Port.S4)
        except:
            pass

        try:
            if ultraSensorDrive == '1':
                self.ultraSensorDrive = UltrasonicSensor(Port.S1)
            elif ultraSensorDrive == '2':
                self.ultraSensorDrive = UltrasonicSensor(Port.S2)
            elif ultraSensorDrive == '3':
                self.ultraSensorDrive = UltrasonicSensor(Port.S3)
            elif ultraSensorDrive == '4':
                self.ultraSensorDrive = UltrasonicSensor(Port.S4)
        except:
            pass
        
        try:
            if ballColorFront == '1':
                self.ballColorFront = ColorSensor(Port.S1)
            elif ballColorFront == '2':
                self.ballColorFront = ColorSensor(Port.S2)
            elif ballColorFront == '3':
                self.ballColorFront = ColorSensor(Port.S3)
            elif ballColorFront == '4':
                self.ballColorFront = ColorSensor(Port.S4)
        except:
            pass

        try:
            if ballColorBack == '1':
                self.ballColorBack = ColorSensor(Port.S1)
            elif ballColorBack == '2':
                self.ballColorBack = ColorSensor(Port.S2)
            elif ballColorBack == '3':
                self.ballColorBack = ColorSensor(Port.S3)
            elif ballColorBack == '4':
                self.ballColorBack = ColorSensor(Port.S4)
        except:
            pass

        print("Settings. Ok!")
    
    def driveAlongLine(self, right, dist, speed):
        turn = 40
        black_cnt = 0
        if right:
            while (self.ultraSensorDrive.distance() > dist):
                if (self.driveColor.color() == Color.BLACK):
                    self.lDriveMotor.run(speed - turn)
                    self.rDriveMotor.run(speed + turn)
                    black_cnt += 1
                else:
                    self.lDriveMotor.run(speed + turn)
                    self.rDriveMotor.run(speed - turn)
                    black_cnt = 0
                if black_cnt == 1:
                    turn = max(turn - 10, 0)
                    remake = False
        else:
            while (self.ultraSensorDrive.distance() > dist):
                if (self.driveColor.color() == Color.BLACK):
                    self.lDriveMotor.run(speed + turn)
                    self.rDriveMotor.run(speed - turn)
                    black_cnt += 1
                else:
                    self.lDriveMotor.run(speed - turn)
                    self.rDriveMotor.run(speed + turn)
                    black_cnt = 0
                if black_cnt == 1:
                    turn = max(turn - 10, 0)
                    remake = False

        self.lDriveMotor.brake()
        self.rDriveMotor.brake()
    
    def moveRail(self, pos):

        if (pos == 'start'):
            self.yRailMotor.run_angle(1000, -110)
        elif (pos == 'startCheckBase'):
            self.xRailMotor.run_angle(1000, -500)
        elif (pos == 'endCheckBase'):
            self.xRailMotor.run_angle(1000, 500)
        elif (pos == 'end'):
            self.yRailMotor.run_angle(1000, 110)
        elif (pos == 'startCheckBalls'):
            self.yRailMotor.run_angle(1000, -565)
        elif (pos == 'endCheckBalls'):
            self.yRailMotor.run_angle(1000, 565)
        elif (pos == 'collectBall'):
            self.yRailMotor.run_angle(1000, 450)
            self.yRailMotor.run_angle(1000, -450)

    def turnRight(self):
        self.lDriveMotor.run_angle(400, -180, Stop.HOLD, False)
        self.rDriveMotor.run_angle(400, 180)

    def turnLeft(self):
        self.lDriveMotor.run_angle(400, 180, Stop.HOLD, False)
        self.rDriveMotor.run_angle(400, -180)

    def turn180edge(self):
        self.lDriveMotor.run_angle(400, 390, Stop.HOLD, False)
        self.rDriveMotor.run_angle(400, -390)
   
    def turnToCheckPole(self, speed):
        self.lDriveMotor.run_angle(200, -240, Stop.HOLD, False)
        self.rDriveMotor.run_angle(500, -600)
        self.lDriveMotor.run_angle(speed, -350)

        for j in range(3):
            self.yRailMotor.run_angle(1000, 100)
            self.bay_colors[0][j] = self.ballColorFront.color()
            print(self.bay_colors[0][j])
            if (self.bay_colors[0][j] != Color.WHITE and self.bay_colors[0][j] != Color.BLACK):
                    self.que_colors[checkColor(self.bay_colors[0][j])] = (0, j)
            self.yRailMotor.run_angle(1000, -100)
            if j == 1:
                self.yRailMotor.run_angle(1000, -130)
                self.xRailMotor.run_angle(1000, -1300)
                self.bay_colors[1][1] = self.ballColorFront.color()
                if (self.bay_colors[1][1] != Color.WHITE and self.bay_colors[1][1] != Color.BLACK):
                    self.que_colors[checkColor(self.bay_colors[1][1])] = (1,1)
                self.xRailMotor.run_angle(1000, 1300)
                self.yRailMotor.run_angle(1000, 130)
            self.lDriveMotor.run_angle(speed, -160, Stop.HOLD, False)
            self.rDriveMotor.run_angle(speed, -160)

        self.lDriveMotor.run_angle(speed, -100, Stop.HOLD, False)
        self.rDriveMotor.run_angle(speed, -100)
        self.lDriveMotor.run_angle(speed, -350)

        for j in range(3):
            if j > 0:
                self.yRailMotor.run_angle(1000, 100)
                self.bay_colors[j][2] = self.ballColorFront.color()
                if (self.bay_colors[j][2] != Color.WHITE and self.bay_colors[j][2] != Color.BLACK):
                    self.que_colors[checkColor(self.bay_colors[j][2])] = (j, 2)
                self.yRailMotor.run_angle(1000, -100)
            self.lDriveMotor.run_angle(speed, -145, Stop.HOLD, False)
            self.rDriveMotor.run_angle(speed, -145)

        self.lDriveMotor.run_angle(speed, -140, Stop.HOLD, False)
        self.rDriveMotor.run_angle(speed, -140)
        self.lDriveMotor.run_angle(speed, -350)

        for j in range(3):
            if (j > 0):
                self.yRailMotor.run_angle(1000, 100)
                self.bay_colors[2][2-j] = self.ballColorFront.color()
                if (self.bay_colors[2][2-j] != Color.WHITE and self.bay_colors[2][2-j] != Color.BLACK):
                    self.que_colors[checkColor(self.bay_colors[2][2-j])] = (2, 2-j)
                self.yRailMotor.run_angle(1000, -100)
            self.lDriveMotor.run_angle(400, -130, Stop.HOLD, False)
            self.rDriveMotor.run_angle(400, -130)

        self.lDriveMotor.run_angle(speed, -140, Stop.HOLD, False)
        self.rDriveMotor.run_angle(speed, -140)
        self.lDriveMotor.run_angle(speed, -350)

        for j in range(3):
            if j > 0:
                self.yRailMotor.run_angle(1000, 100)
                self.bay_colors[2-j][0] = self.ballColorFront.color()
                if (self.bay_colors[2-j][0] != Color.WHITE and self.bay_colors[2-j][0] != Color.BLACK):
                    self.que_colors[checkColor(self.bay_colors[2-j][0])] = (2-j, 0)
                self.yRailMotor.run_angle(1000, -100)
            self.lDriveMotor.run_angle(speed, -130, Stop.HOLD, False)
            self.rDriveMotor.run_angle(speed, -130)

        self.lDriveMotor.run_angle(speed, -200, Stop.HOLD, False)
        self.rDriveMotor.run_angle(speed, -200)
        self.lDriveMotor.run_angle(speed, -350)

    def rideToStorage(self, speed):
        self.lDriveMotor.run_angle(speed, -630, Stop.HOLD, False)
        self.rDriveMotor.run_angle(speed, -630)
        self.turnRight()
        while (self.driveColor.color() != Color.BLACK):
            self.lDriveMotor.run(-250)
            self.rDriveMotor.run(-250)
        self.lDriveMotor.brake()
        self.rDriveMotor.brake()
        self.lDriveMotor.run_angle(speed, -60, Stop.HOLD, False)
        self.rDriveMotor.run_angle(speed, -60)
        self.turnLeft()
        self.driveAlongLine(True, 185, -200)
        self.moveRail('startCheckBalls')
        self.lDriveMotor.run_angle(200, -240, Stop.HOLD, False)
        self.rDriveMotor.run_angle(485, -600)
        self.lDriveMotor.run_angle(200, 105, Stop.HOLD, False)
        self.rDriveMotor.run_angle(200, 105)

        self.collectBalls(80, True)

    def collectBalls(self, speed, isFront):
        balls_count = 0
        blackLineBe = False
        self.xRailMotor.run_angle(1000, -1180)
        self.lDriveMotor.run(speed)
        self.rDriveMotor.run(speed) 
        while (balls_count < 2):
            if (self.driveColor.color() == Color.BLACK):
                blackLineBe = True
            if (self.ballColorFront.reflection() >= 5):
                self.lDriveMotor.brake()
                self.rDriveMotor.brake()
                if isFront:
                    if balls_count == 0:
                        self.yRailMotor.run_angle(1000, -60)
                        self.xRailMotor.run_angle(1000, -530)
                        self.yRailMotor.run_angle(1000, 60)
                        self.moveRail('collectBall')
                        self.xRailMotor.run_angle(1000, 530)
                    else:
                        self.moveRail('collectBall')
                    isFront = False
                else:
                    pass
                self.xRailMotor.run_angle(1000, 760)
                self.yRailMotor.run_angle(1000, 200)
                balls_count += 1
            elif (self.ballColorFront.reflection() == 0):
                self.lDriveMotor.brake()
                self.rDriveMotor.brake()
                if isFront:
                    self.xRailMotor.run_angle(1000, 760)
                    self.yRailMotor.run_angle(1000, 200)
                    isFront = False
                else:
                    self.yRailMotor.run_angle(1000, -200)
                    self.xRailMotor.run_angle(1000, -760)
                    isFront = True
                self.lDriveMotor.run_angle(speed, 25, Stop.HOLD, False)
                self.rDriveMotor.run_angle(speed, 25)
            self.lDriveMotor.run(speed)
            self.rDriveMotor.run(speed)
                
        self.lDriveMotor.brake()
        self.rDriveMotor.brake()

        if (isFront):
            self.xRailMotor.run_angle(1000, 1100)
        else:
            self.yRailMotor.run_angle(1000, -200)
            self.xRailMotor.run_angle(1000, 340)

        if blackLineBe:
            while self.driveColor.color() != Color.BLACK:
                self.lDriveMotor.run(-speed)
                self.rDriveMotor.run(-speed)
        else:
            while self.driveColor.color() != Color.BLACK:
                self.lDriveMotor.run(speed)
                self.rDriveMotor.run(speed)
        self.lDriveMotor.run_angle(speed, -50, Stop.HOLD, False)
        self.rDriveMotor.run_angle(speed, -50)
        self.turnLeft()
        

        self.driveAlongLine(True, 115, -200)
        self.turn180edge()
        self.lDriveMotor.run_angle(200, 150, Stop.HOLD, False)
        self.rDriveMotor.run_angle(200, 150)
        self.turnRight()
        self.lDriveMotor.run_angle(200, 200, Stop.HOLD, False)
        self.rDriveMotor.run_angle(200, 200)

    def decomposeBalls(self, speed):
        robot_ind = [1, 2]
        is_front = True
        if (self.decomp_que[0][0] < robot_ind[0] and self.decomp_que[0][0] != (1, 1)):
            while (robot_ind != self.decomp_que[0]):
                if (robot_ind[1] == 2 and robot_ind[0] == 0):
                    self.lDriveMotor.run_angle(speed, 140, Stop.HOLD, False)
                    self.rDriveMotor.run_angle(speed, 140)
                    self.lDriveMotor.run_angle(speed, 350)
                    self.lDriveMotor.run_angle(speed, 130, Stop.HOLD, False)
                    self.rDriveMotor.run_angle(speed, 130)
                    robot_ind = [0, 1]
                elif (robot_ind[0] == 0 and robot_ind[1] == 0):
                    self.lDriveMotor.run_angle(speed, 140, Stop.HOLD, False)
                    self.rDriveMotor.run_angle(speed, 140)
                    self.lDriveMotor.run_angle(speed, 350)
                    self.lDriveMotor.run_angle(speed, 130, Stop.HOLD, False)
                    self.rDriveMotor.run_angle(speed, 130)
                    robot_ind = [1, 0]
                elif (robot_ind[1] == 2):
                    self.lDriveMotor.run_angle(speed, 130, Stop.HOLD, False)
                    self.rDriveMotor.run_angle(speed, 130)
                    robot_ind[0] -= 1
                    print('aboba')
                elif (robot_ind[0] == 0):
                    self.lDriveMotor.run_angle(speed, 130, Stop.HOLD, False)
                    self.rDriveMotor.run_angle(speed, 130)
                    robot_ind[1] -= 1
                print(robot_ind)
            


        elif (self.decomp_que[0][0] != (1, 1)):
            while (robot_ind != self.decomp_que[0]):
                pass

            


    def saveColors(self, speed):
        while (self.driveColor.color() != Color.BLACK):
            self.lDriveMotor.run(speed)
            self.rDriveMotor.run(speed)
        self.lDriveMotor.brake()
        self.rDriveMotor.brake()
        for _ in range(4):
             self.lDriveMotor.run_angle(speed, 55, Stop.HOLD, False)
             self.rDriveMotor.run_angle(speed, 55)
             sleep(0.2)
             self.que_colors[checkColor(self.driveColor.color())] = (0, 0)
        print(self.que_colors)
    


def main():
    settings = {'yRailMotor': 'C', 'xRailMotor': 'D', 'lDriveMotor': 'B', 'rDriveMotor': 'A', 'driveColor': '3', 'ultraSensorDrive': '4', 'ballColorFront': '2', 'ballColorBack': '1'}
    robot = Robot(settings['yRailMotor'], settings['xRailMotor'], settings['lDriveMotor'], settings['rDriveMotor'], settings['driveColor'], settings['ultraSensorDrive'], settings['ballColorFront'], settings['ballColorBack'])
    robot.moveRail('start')
    robot.saveColors(-200)
    robot.driveAlongLine(False, 185, -200)
    robot.moveRail('startCheckBase')
    robot.turnToCheckPole(400)
    for value in robot.que_colors:
        robot.decomp_que.append(robot.que_colors[value])
    print(robot.decomp_que)
    robot.moveRail('endCheckBase')
    robot.rideToStorage(300)
    robot.decomposeBalls(400)
    for i in range(3):
        for j in range(3):
            print(robot.bay_colors[i][j], end=' ')
        print('\n')

if __name__ == "__main__":
    main()