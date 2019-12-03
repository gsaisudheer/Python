import sys
import math
import random
from PIL import Image

def dist(x1,y1,x2,y2):
	temp=math.pow(x1-x2,2)+math.pow(y1-y2,2)
	temp=math.sqrt(temp)
	return temp

def main():
	xcord=1000
	ycord=1000
	image=Image.new("RGB", (xcord, ycord))
	p=input("Enter the number of points in the plane\n")
	if p<=0:
		print("Sorry!Invalid Input\n")
		sys.exit()
	else:
		print("The points will be distributed randomly in the xy plane\n")

		xpoints=random.sample(range(xcord),p)
		ypoints=random.sample(range(ycord),p)
		red=[random.randint(0,255) for r in xrange(p)]
		blue=[random.randint(0,255) for r in xrange(p)]
		green=[random.randint(0,255) for r in xrange(p)]
		for i in range(xcord):
			for j in range(ycord):
				listOfDists=[] 
				for k in range(p):
					listOfDists.append(dist(i,j,xpoints[k],ypoints[k]))
				minIndex=listOfDists.index(min(listOfDists))
				image.putpixel((i,j),(red[minIndex],blue[minIndex],green[minIndex]))
			
		for i in range(p):
			image.putpixel((xpoints[i],ypoints[i]),(255-red[i%255],255-blue[i%255],255-green[i%255]))

		image.save('vornoi1000new.png')

if __name__=='__main__': main()
