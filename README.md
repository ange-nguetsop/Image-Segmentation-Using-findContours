### Introduction
This project aims to develop a system capable of detecting and tracking a specific object based on its color, applicable to both still images and videos using findContours algorithm. FindContours is a function provided by the OpenCV library in Python. It is used to detect and extract contours from binary images, which can be useful for various computer vision tasks like object detection, image segmentation, and shape analysis.


### Objectives
- **Color Detection**: Isolate a specific object (like a tomato) in an image using its color.
- **Object Tracking**: Track this object in a video sequence.
- **Object Identification**: Under certain conditions, specify the nature of the detected object.

## Output
![Result](https://github.com/ange-nguetsop/ObjectTracking/blob/master/result1.png)

### Challenges and Solutions
1. **Calibration of HSV Values**
   The first challenge was to find the optimal HSV values to isolate the desired color under various lighting conditions. For this, a function for manual adjustment of HSV values was used, testing on multiple photos taken under varied conditions. After numerous trials, the ideal values were determined and then we have this result:
![Result](https://github.com/ange-nguetsop/ObjectTracking/blob/master/zwischenErgebnis.png)   

3. **Detection of Closed Contours**
   A major issue encountered was forcing the algorithm to detect only closed contours. Various image processing techniques such as erosion, dilation, and thresholding were applied to achieve closed contours, a crucial step for the system's accuracy. The image before the use of cv2.findContours is:
![Result](https://github.com/ange-nguetsop/ObjectTracking/blob/master/zwischen2.png)

5. **Filtering of Contours**
   After obtaining closed contours, it was necessary to filter the internal contours to keep only the most external ones. This step effectively isolated the object of interest.

### Results
The developed system successfully identified and clearly encircled tomatoes in various images and could even count the number of tomatoes detected by the system. The system is adaptable and can be modified to isolate other fruits or vegetables, such as avocados or oranges.

## Issues
However, the cv2.findContours algorithm has its limitations, as it was impossible to accurately identify tomatoes when they were clustered together. In such cases, it is preferable to use the watershed method, which is specifically designed to address this type of issue.
An Example where the system failed to accurately identify tomatoes:

![Beispiel](https://github.com/ange-nguetsop/ObjectTracking/blob/master/result2.png)


Here you can see how to solve this problem with the watershed method: [https://github.com/ange-nguetsop/ImageSegmentation001]
But you can already see the result here: 
![Alt Watershed](https://github.com/ange-nguetsop/ObjectTrackingWithFindContours/blob/master/Watershed.png)

### Possibilities for Improvement
- **Automation of HSV Value Determination**: Development of an algorithm to automatically adjust HSV values based on the object (fruit or vegetable) to be detected and isolated.
- **Advanced Object Identification**: Improvement of the system to identify the object based on parameters such as shape, color, and area, under certain conditions.

### Conclusion
This project demonstrates the effectiveness of image processing and computer vision techniques in detecting and tracking specific objects. Although the current system is focused on tomato detection, its flexibility and potential for extension make it a powerful tool for various industrial, commercial, and educational applications.
