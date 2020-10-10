import cv2
import numpy as np
import math

fields=3
#Number of fields
field=['name','position','project']
#The values to be put in the blanks
img = cv2.imread('certif.jpeg')
#the template being fed in
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,250,250,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
t1=0
t2=0
count=0
for line in lines:
    x1=line[0][0]
    y1=line[0][1]
    x2=line[0][2]
    y2=line[0][3]
    slope=(float)(y2-y1)/(x2-x1)
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 

    if(slope==0 and (dist>=100.0 and dist<=400.0)):
        if((t1==0 and t2==0) or abs(x1-t1)>=20 or abs(y1-t2)>=100):
            cv2.line(img,(line[0][0],line[0][1]),(line[0][2],line[0][3]),(0,255,0),2)
            t1=x1
            t2=y1
            count=count+1
            cv2.putText(img,field[len(field)-count], ((x1+5),(y1-10)),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 0, 0),1, cv2.LINE_AA)
            if(count==fields):
                break

#store the generated certificate in the file system
cv2.imwrite('certif.jpg',img)
#Display the generated certificate in a window
cv2.imshow('Certificate',img)
cv2.waitKey(0)
