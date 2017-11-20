'''
Chris Benson
12/11/2015

A library of shapes to use when building VUV geometry

'''
import random

def inTomm(inch):
            return inch*25.4

class geoVolume:
    def __init__(self,centerCoords={'x':0,'y':0,'z':0}):
        self.center = centerCoords
        self.material = 'pmt_vacuum'
        self.mother = 'world'
        self.invisible = 1
        self.colorVect = [random.random(),random.random(),random.random(),0.5]
        self.drawstyle = 'solid'


class boxVolume(geoVolume):
    def __init__(self,name,height,width,depth):
        geoVolume.__init__(self)
        self.name = name
        self.height = height
        self.width = width
        self.depth = depth
        self.volType = 'box'
        self.invisible = 0
        self.rotation = [0,0,0]

    def writeToString(self,OutputString):
        OutputString += '\n{\nname: "GEO",\nindex: "'+self.name+'",\nvalid_begin: [0,0],\nvalid_end: [0,0],\n'
        OutputString += 'type: "'+self.volType+'",\n'
        OutputString += 'mother: "'+self.mother+'",\n'
        OutputString += 'size: ['+str(inTomm(float(self.height))/2.0)+','+str(inTomm(float(self.width))/2.0)+','+str(inTomm(float(self.depth))/2.0)+'],\n'
        OutputString += 'position: ['+str(inTomm(float(self.center['x'])))+','+str(inTomm(float(self.center['y'])))+','+str(inTomm(float(self.center['z'])))+'],\n'
        OutputString += 'rotation: ['+str(float(self.rotation[0]))+','+str(float(self.rotation[1]))+','+str(float(self.rotation[2]))+'],\n'
        OutputString += 'material: "'+self.material+'",\n'
        OutputString += 'color: ['+str(self.colorVect[0])+','+str(self.colorVect[1])+','+str(self.colorVect[2])+','+str(self.colorVect[3])+'],\n'
        OutputString += 'drawstyle: "solid",\n'
        OutputString += 'invisible: '+str(int(self.invisible))+',\n}\n'

        return OutputString

# I modified this to include phi_start and phi_delta
class tubeVolume(geoVolume):
    def __init__(self,name,rMax,height,rMin=0, phi_start=0.0, phi_delta=360.0):
        geoVolume.__init__(self)
        self.name = name
        self.rMax = rMax
        self.rMin = rMin
        self.height = height
        self.volType = 'tube'
        self.invisible = 0
        self.rotation = [0.0,0.0,0.0]
        self.phi_start = phi_start
        self.phi_delta = phi_delta

    def writeToString(self,OutputString):
        OutputString += '\n{\nname: "GEO",\nindex: "'+self.name+'",\nvalid_begin: [0,0],\nvalid_end: [0,0],\n'
        OutputString += 'type: "'+self.volType+'",\n'
        OutputString += 'mother: "'+self.mother+'",\n'
        OutputString += 'r_max: '+str(inTomm(float(self.rMax)))+',\n'
        OutputString += 'r_min: '+str(inTomm(float(self.rMin)))+',\n'
        OutputString += 'size_z: '+str(inTomm(float(self.height))/2.0)+',\n'
        OutputString += 'phi_start: '+str(self.phi_start)+',\n'
        OutputString += 'phi_delta: '+str(self.phi_delta)+',\n'
        OutputString += 'position: ['+str(inTomm(float(self.center['x'])))+','+str(inTomm(float(self.center['y'])))+','+str(inTomm(float(self.center['z'])))+'],\n'
        OutputString += 'rotation: ['+str(float(self.rotation[0]))+','+str(float(self.rotation[1]))+','+str(float(self.rotation[2]))+'],\n'
        OutputString += 'material: "'+self.material+'",\n'
        OutputString += 'color: ['+str(self.colorVect[0])+','+str(self.colorVect[1])+','+str(self.colorVect[2])+','+str(self.colorVect[3])+'],\n'
        OutputString += 'drawstyle: "solid",\n'
        OutputString += 'invisible: '+str(int(self.invisible))+',\n}\n'
        return OutputString

# I added this
class sphereVolume(geoVolume):
    def __init__(self, name, rMax, rMin, theta_start = 0, theta_delta = 180., phi_start=0.0, phi_delta=360.0):
        geoVolume.__init__(self)
        self.name = name
        self.rMax = rMax
        self.rMin = rMin
        self.theta_start = theta_start
        self.theta_delta = theta_delta
        self.phi_start = phi_start
        self.phi_delta = phi_delta
        self.volType = 'sphere'
        self.invisible = 0
        self.rotation = [0.0, 0.0, 0.0]

    def writeToString(self, OutputString):
        OutputString += '\n{\nname: "GEO",\nindex: "' + self.name + '",\nvalid_begin: [0,0],\nvalid_end: [0,0],\n'
        OutputString += 'type: "' + self.volType + '",\n'
        OutputString += 'mother: "' + self.mother + '",\n'
        OutputString += 'r_max: ' + str(inTomm(float(self.rMax))) + ',\n'
        OutputString += 'r_min: ' + str(inTomm(float(self.rMin))) + ',\n'
        OutputString += 'theta_start: ' + str(self.theta_start) + ',\n'
        OutputString += 'theta_delta: ' + str(self.theta_delta) + ',\n'
        OutputString += 'phi_start: ' + str(self.phi_start) + ',\n'
        OutputString += 'phi_delta: ' + str(self.phi_delta) + ',\n'
        OutputString += 'position: [' + str(inTomm(float(self.center['x']))) + ',' + str(
            inTomm(float(self.center['y']))) + ',' + str(inTomm(float(self.center['z']))) + '],\n'
        OutputString += 'rotation: [' + str(float(self.rotation[0])) + ',' + str(
            float(self.rotation[1])) + ',' + str(float(self.rotation[2])) + '],\n'
        OutputString += 'material: "' + self.material + '",\n'
        OutputString += 'color: [' + str(self.colorVect[0]) + ',' + str(self.colorVect[1]) + ',' + str(
            self.colorVect[2]) + ',' + str(self.colorVect[3]) + '],\n'
        OutputString += 'drawstyle: "solid",\n'
        OutputString += 'invisible: ' + str(int(self.invisible)) + ',\n}\n'
        return OutputString


#### Classes for a border
class border:
    def __init__(self,name,volume1,volume2):
        # to find more surfaces to choose from, refer to $RATROOT/data/OPTICS.ratdb
        self.surface = 'stainless_steel'
        self.mother = 'world'
        self.vol1 = volume1
        self.vol2 = volume2
        self.name = name
        self.volType = 'border'
        self.colorVect = [random.random(),random.random(),random.random(),0.5]
        self.invisible = 0
        self.drawstyle = 'solid'

    def writeToString(self,OutputString):
        OutputString += '\n{\nname: "GEO",\nindex: "'+self.name+'",\nvalid_begin: [0,0],\nvalid_end: [0,0],\n'
        OutputString += 'type: "'+self.volType+'",\n'
        OutputString += 'mother: "'+self.mother+'",\n'
        OutputString += 'volume1: "'+self.vol1+'",\n'
        OutputString += 'volume2: "'+self.vol2+'",\n'
        OutputString += 'surface: "'+self.surface+'",\n'
        OutputString += 'color: ['+str(self.colorVect[0])+','+str(self.colorVect[1])+','+str(self.colorVect[2])+','+str(self.colorVect[3])+'],\n'
        OutputString += 'drawstyle: "solid",\n'
        OutputString += 'invisible: '+str(int(self.invisible))+',\n}\n'
        return OutputString






