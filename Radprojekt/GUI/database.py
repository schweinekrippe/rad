#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  database.py
#  
#  Copyright 2017 Topfpflanze <Topfpflanze@WINTERGARTEN>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sqlite3
import os
import random
import datetime
import thread
import Queue
import time
import pickle as pickle



# Handles the data extraction from the database.
class databaseReader():
    def __init__(self, databasepath):
        self.databasepath = databasepath
        self.isConnected = False
        self.connectToDB()
        
    # tries to connect to the databe.
    def connectToDB(self):
        if os.path.isfile(self.databasepath):
            self.conn = sqlite3.connect(self.databasepath)
            self.c = self.conn.cursor()
            self.isConnected = True

        else:
            print("no database found")
            
    def getSpeed(self):
        
        dates = []
        velocities = []
        
        temp = self.c.execute("SELECT * FROM speed ORDER BY ROWID")
        for row in temp:
            dates.append(row[0])
            velocities.append(row[1])
            
        return(dates, velocities)
        
    def getSteeringAngle(self):
        
        dates = []
        angles = []
        
        temp = self.c.execute("SELECT * FROM steeringAngle ORDER BY ROWID")
        for row in temp:
            dates.append(row[0])
            angles.append(row[1])
            
        return(dates, angles)
        
    def getImuData(self):
        
        dates = []
        orientationX = []
        orientationY = []
        orientationZ = []
        angularVelocityX = []
        angularVelocityY = []
        angularVelocityZ = []
        linAccelerationX = []
        linAccelerationY = []
        linAccelerationZ = []
        
        temp = self.c.execute("SELECT * FROM imu ORDER BY ROWID")
        for row in temp:
            dates.append(row[0])
            angularVelocityX.append(row[1])
            angularVelocityY.append(row[2])
            angularVelocityZ.append(row[3])
            orientationX.append(row[4])
            orientationY.append(row[5])
            orientationZ.append(row[6])
            linAccelerationX.append(row[7])
            linAccelerationY.append(row[8])
            linAccelerationZ.append(row[9])
            
        return(dates, angularVelocityX, angularVelocityY, angularVelocityZ, orientationX, orientationY, orientationZ, linAccelerationX, linAccelerationY, linAccelerationZ)
        
    def getCommands(self):
        
        dates = []
        types = []
        values = []
        
        temp = self.c.execute("SELECT * FROM commands ORDER BY ROWID")
        for row in temp:
            dates.append(row[0])
            types.append(row[1])
            values.append(pickle.loads(str(row[2])))
            
        return(dates, types, values)
 

class databaseWriter():
    

    def __init__(self, createDummy=False):
        # read the config file and execute the statements
        fl = open("config.txt", "r")
        for line in fl:
            exec(line)
        
        self.databasePath = DBPATH
        self.MAXEXBFCOM = MAXEXBFCOM
        
        # Queue of data that should be written to the database
        self.Q = Queue.Queue()
        
        thread.start_new_thread( self.__dbWriter__, ())
        
        if createDummy:
            thread.start_new_thread(self.createDummyData, (30,))
        


    
    
    # start in an own process
    def __dbWriter__(self):
        
        # Check if database exists. If not create it
        if not os.path.isfile(self.databasePath):    
            self.__createDatabase__()
        
        # connect to database
        conn = sqlite3.connect(self.databasePath)
        c = conn.cursor()

        
        counter = 0

        while True:
            
            item = self.Q.get()
            counter += 1
            
            # add an element t0 the table with the key = item[0]
            c.execute('INSERT INTO ' + item[0] + ' VALUES (' + ('?,'*len(item[1]))[0:-1] + ')', item[1])
            
            # commit if the queue is empty or the maximum of executions is reached
            # this secures a fast processing and a secure storage without the risk of corruption
            if self.Q.empty() or counter == self.MAXEXBFCOM:
                conn.commit()
                counter = 0
                print("commie")


                
    
    
    ## Add data to the database
    
    def addIMUData(self, acceleration, orientation, rotation):
    
        [accelerationx, accelerationy, accelerationz] = acceleration
        [orientationx, orientationy, orientationz] = orientation
        [rotationx, rotationy, rotationz] = rotation
        item = ["imu", (time.time(), accelerationx, accelerationy, accelerationz, orientationx, orientationy, orientationz, rotationx, rotationy, rotationz)]
        self.Q.put(item)
        
    def addGPSData(self, longitude, latitude):
        item = ["gps", (time.time(), longitude, latitude)]
        self.Q.put(item)
        
    def addCommand(self, commandType, value=None):
        
        item = ["commands", (time.time(), commandType, sqlite3.Binary(pickle.dumps(value, -1)))]
        self.Q.put(item)
        
    def addSpeed(self, speed):
        item = ["speed", (time.time(), speed)]
        self.Q.put(item)
        
    def addSteeringAngle(self, angle):
        item = ["steeringAngle", (time.time(), angle)]
        self.Q.put(item)
        
    def addObstData(self, obstacles):
        item = ["obstacles", (time.time(), sqlite3.Binary(pickle.dumps(obstacles, -1)))]
        self.Q.put(item)

    ## Add dummy data

    def createDummyData(self, iterations):
        for i in range (iterations):
            
            self.addIMUData([random.gauss(0, 0.5), random.gauss(0, 0.5), random.gauss(0, 0.5)], [random.gauss(0, 0.5), random.gauss(0, 0.5), random.gauss(0, 0.5)], [random.gauss(0, 0.5), random.gauss(0, 0.5), random.gauss(0, 0.5)])
            self.addGPSData(random.gauss(0, 0.5)*360, random.gauss(0, 0.5)*360)
            
            if random.randint(0,10) < 3:
                ctype = random.choice(["tgtSpeed", "tgtAngle", "stop", "limits"])
                if ctype == "limits":
                    rnd1 = random.randint(-10,10)
                    rnd2 = random.gauss(0, 0.5)
                    limits = [rnd1-rnd2, rnd1+rnd2]
                
                    self.addCommand(ctype, limits)
                elif ctype == "stop":
                    self.addCommand(ctype)
                
                elif ctype == "tgtSpeed":
                    self.addCommand(ctype, random.random()*25)
                else:
                    self.addCommand(ctype, random.random()*180 -90)
            self.addSpeed(abs(random.gauss(0, 0.5))*2.5)
            self.addSteeringAngle(random.gauss(0, 0.5)*180 -90)
            time.sleep(0.01)
    
    # create a database
    
    def __createDatabase__(self):
        
        conn = sqlite3.connect(self.databasePath)
        c = conn.cursor()
        c.execute('''CREATE TABLE imu
             (date, angularVelocityX, angularVelocityY, angularVelocityZ, orientationX, orientationY, orientationZ, linAccelerationX, linAccelerationY, linAccelerationZ)''')
        c.execute('''CREATE TABLE gps
             (date, longitude, latitude)''')
        c.execute('''CREATE TABLE commands
             (date, type, value)''')  # types: tgtSpeed, tgtAngle, stop, limits
        c.execute('''CREATE TABLE speed
             (date, speed)''')
        c.execute('''CREATE TABLE steeringAngle
             (date, steeringAngle)''')
        c.execute('''CREATE TABLE obstacles
             (date, obstacles)''')
        conn.commit()
        conn.close()

    

def main(args):
  
    W = databaseWriter(createDummy=True)

    
    raw_input("press return to continue")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
