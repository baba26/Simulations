from visual import vector,mag,norm



from visual import sphere,rate,color,display
from math import cos,sin,pi
from numpy import arange

d = display()

m_earth = 100.0
m_sun = 10000000.0

g = 0.000001

r = vector(70.0,0,0)
v = vector(0,2.0,0)

s_earth = sphere(pos=[r.x,r.y,r.z],radius=1,color = color.white)

s_sun = sphere(pos=[0,0,0],radius=2,color = color.yellow)

d.autoscale = False
 
while True:
    rate(30)
    a = -1*norm(r)*((g*m_earth*m_sun)/(mag(r)**2))
    v = v + a
    r = r + v
    s_earth.pos = [r.x,r.y,r.z]
