from visual import vector,mag,norm



from visual import sphere,rate,color,display,cylinder
from math import cos,sin,pi
from numpy import arange

d = display()

m_earth = 100.0
m_sun = 10000000.0

g = 1.8

r = vector(0,30,0)
v = vector(0,0,0)

framerate = 60
t = 1.0/framerate
s_earth = sphere(pos=[r.x,r.y,r.z],radius=1,color = color.white)
'''
s_sun = sphere(pos=[0,0,0],radius=2,color = color.yellow)
'''
#d.autoscale = False
rod = cylinder(pos=(-50,0,0), axis=(100,0,0), radius=0.1)

while True:
    rate(framerate)
    a = vector(0,-1*g,0)
    v = v + t*a
    r = r + v
    if( r.y < 0 ):
        v.y = -1*v.y
        r.y = -1*r.y
        print v.y
    s_earth.pos = [r.x,r.y,r.z]
