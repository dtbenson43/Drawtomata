from math import sin, cos, radians, acos, sqrt, pi, atan2, degrees

def pointPos(x0, y0, d, angle):
    theta_rad = pi/2 - radians(angle)
    return (x0 + d*cos(theta_rad), y0 + d*sin(theta_rad))

def distance(A, B):
  newA = (B[0] - A[0], B[1] - A[1])
  newB = (A[0] - B[0], A[1] - B[1])
  return length(newA)

def length(v):
  return sqrt(v[0]**2+v[1]**2)

def dotProduct(v,w):
  return v[0]*w[0]+v[1]*w[1]

def determinant(v,w):
  return v[0]*w[1]-v[1]*w[0]

def innerAngle(v,w):
  cosx=dotProduct(v,w)/(length(v)*length(w))
  if cosx > 1:
    cosx = 1
  if cosx < -1:
    cosx = -1
  rad=acos(cosx)
  return rad*180/pi

def angleBase(A, B):
  rads = atan2(B[1]-A[1], B[0]-A[0])
  degs = degrees(rads)
  return degs

def angleClockwise(A, B):
  rads = atan2(B[1]-A[1], B[0]-A[0])
  degs = degrees(rads)
  if degs<0: 
      return 360 + degs
  else:
      return degs


def roundDown(num, multiple):
  return num - (num % multiple)

def roundUp(num, multiple):
  rem = num % multiple
  return num if rem == 0 else num + multiple - rem