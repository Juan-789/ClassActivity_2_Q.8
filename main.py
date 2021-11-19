"""
8. H hours, M minutes and S seconds have passed since midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Ask the user to input the H, M, S and determine the angle (in degrees) of the hour hand on the clock face.
"""

def angle():
  hours = int(input("hours " ))
  minutes = int(input("Minutes "))
  seconds = int(input("Seconds "))
  degrees = (hours +(minutes/60)+(seconds/3600))*30
  degrees = degrees%360
  print (degrees)
#angle()