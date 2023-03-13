import time
import random
def east():
    east.st=1
    east.r=1
    print('east side can go straight')
    print('east side can go right')
    west.st=0
    west.r=0
    north.st=0
    north.r=0
    south.st=0
    south.r=0
def west():
    east.st=0
    east.r=0
    west.st=1
    west.r=1
    print('west side can go straight')
    print('west side can go right')
    north.st=0
    north.r=0
    south.st=0
    south.r=0
def north():
    east.st=0
    east.r=0
    west.st=0
    west.r=0
    north.st=1
    north.r=1
    print('north side can go straight')
    print('north side can go right')
    south.st=0
    south.r=0
def south():
    east.st=0
    east.r=0
    west.st=0
    west.r=0
    north.st=0
    north.r=0
    south.st=1
    south.r=1
    print('south side can go straight')
    print('south side can go right')

while 1:
    east();
    time.sleep(3)
    print('|')
    print('|')
    print('|')
    west();
    time.sleep(3)
    print('|')
    print('|')
    print('|')
    north();
    time.sleep(3)
    print('|')
    print('|')
    print('|')
    south();
    time.sleep(3)
    print('|')
    print('|')
    print('|')

