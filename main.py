import numpy as np
import cv2

image = cv2.imread('Tomate3.jpg')
result = image.copy()
image = cv2.GaussianBlur(image,(11,11),0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0,77,42])
upper = np.array([18,255,255])
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(result,result, mask= mask)
output = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(output,30,255,cv2.THRESH_BINARY)
    
    # noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 4)
    
    # Opérations morphologiques pour fusionner les régions proches
kernel1 = np.ones((7,7), np.uint8)  # La taille du noyau affecte le degré de fusion
dilated = cv2.dilate(thresh, kernel1, iterations=4)  # Augmenter les iterations pour plus de fusion

    #eroded = cv2.erode(dilated, kernel, iterations=4)  # Ajuster les iterations selon les besoins
kernel2 = np.ones((9,9), np.uint8)  # La taille du noyau affecte le degré de fusion
eroded = cv2.erode(dilated, kernel2, iterations= 5)

contours, hierarchy = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

area = []
for i in range (0, len(contours)):
    area.append(cv2.contourArea(contours[i]))

area_np = np.array([area])
    
  
mean = area_np.mean()
        
index = []
for i in range (0, len(area)):
    if area[i] >= mean + (0.01 * mean) or area[i] <=  mean + (0.01 * mean):
            index.append(i)

topmost = []
for i in index:
    cnt = contours[i]
    topmost.append(tuple(cnt[cnt[:,:,1].argmin()][0]))


center = []
for i in range (0,len(index)):
    cnt = contours[i]
    M = cv2.moments(cnt)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        center.append([cx,cy])

radius = []

for i in range(0,len(center)):
    r = (center[i][0]-topmost[i][0]) ** 2 + (center[i][1]-topmost[i][1]) ** 2
    r = r ** (1/2)
    radius.append(int(r))


        # Parcourir tous les contours trouvés
for i in range (0,len(center)):
    cv2.circle(img = result, center = center[i], radius = radius[i] + 10, color =  (0, 255, 0) , thickness = 5, lineType = cv2.LINE_AA)
cv2.imwrite('result2.png',result)
cv2.imshow('result', result)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
