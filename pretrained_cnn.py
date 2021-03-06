#########################Face Detection using Pretrained cnn####################
from PIL import Image           # To load images from files
from imutils import face_utils  # This package provides funcions (translation, rotation, resizing and displaying Matplotlib images easier with OpenCV and Python)
import matplotlib.pyplot as plt # To display images
import numpy as np 
import dlib                     # To detect facial landmarks 
import cv2                      # For detection of faces and its features, to draw bounding box
import tensorflow as tf
import argparse 
import os
import time

def write_to_disk(image, face_cordinates):
    '''
    This function will save the cropped image from original photo to disk
    '''
    for (x1, y1, w, h) in face_cordinates:
        cropped_face = image[y1:y1 + h, x1:x1 + w]
        cv2.imwrite(str(y1) + ".jpg", cropped_face)#imwrite() is an OpenCV function

w = "mmod_human_face_detector.dat"

# initialize cnn based face detector with the weights
cnn_face_detector = dlib.cnn_face_detection_model_v1(w) #cnn_face_detection_model_v1() is dlib function to detect face using pretrained cnn
image = cv2.imread('test_image1.jpg')
gray = tf.image.rgb_2_grayscale(image)
#gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply face detection (cnn)
start = time.time()
faces_cnn = cnn_face_detector(image, 1)
end = time.time()
print("Time taken by Pretrained CNN  to detect face: ", format(end - start, '.2f'))

    
# CNN
for (i, face) in enumerate(faces_cnn):
  # Find points to draw rectangle on face
  x, y, w, h = face.rect.left(), face.rect.top(), face.rect.width(), face.rect.height()
  # Draw rectangle around detected face
  cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
  # Scan detected face (faces_cnn) from top left corner and resize it using shape() funtion to fit it into rectangle
  img_height, img_width = image.shape[:2]
 
 # To combine detected face & bounding box 
  cv2.putText(image, "", (img_width - 200, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
              (0, 255, 0), 2)
  # To display the image
  plt.imshow(image)
  plt.show()
  #cv2.imshow('Output', image)
  #cv2.waitKey()
  #cv2.destroyAllWindows()
#####################################################################

################Facial Landmarking using Pretrained CNN##############

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt   #conda install -c conda-forge matplotlib
import matplotlib.image as image  # To display images
import numpy as np
import dlib                       # To detect facial landmarks #conda install -c menpo dlib
import tensorflow as tf
import cv2                        # For detection of faces and its features, to draw bounding box 
                                  #conda install -c conda-forge opencv
import argparse
import os
from image_utility import save_image, generate_random_color, draw_border
from imutils import face_utils    # This package provides funcions (translation, rotation, resizing and displaying Matplotlib images easier with OpenCV and Python)
                                  #conda install -c conda-forge python-utils

w = "shape_predictor_68_face_landmarks.dat"
# landmark predictor
predictor = dlib.shape_predictor(w)

d = "mmod_human_face_detector.dat"
cnn_face_detector = dlib.cnn_face_detection_model_v1(d)
p = "deploy.prototxt.txt" #deploy.prototxt.txt contains architecture of CNN
m = "res10_300x300_ssd_iter_140000.caffemodel" 
face_detector = cv2.dnn.readNetFromCaffe(p, m)
image = cv2.imread('test_image4.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces_cnn = cnn_face_detector(gray, 1)

# CNN
for (i, face) in enumerate(faces_cnn):
  # Find points to draw rectangle on face
  x, y, w, h = face.rect.left(), face.rect.top(), face.rect.width(), face.rect.height()
  # Draw rectangle around detected face
  cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
  
  shape = predictor(gray, face.rect)    #facial features are extracted
  shape = face_utils.shape_to_np(shape) #ROIs are extracted and stored in shape
  # Draw detected cordinate points (x,y) on ROI image
  for (x, y) in shape:
    cv2.circle(image, (x, y), 2, (0, 255, 0), -1) # To show landmarks on ROI

#To display face with detected landmarks
plt.imshow(image)
plt.show()
    #cv2.imshow('Output', image)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
################################################################################

###################Euclidean Distance#####################
import numpy as np
import argparse
import imutils
import cv2
import math  

#Forehead Distance
p1 = [191,173]
p2 = [252,187]
#Left and Right eyes (Exocanthion to Exocanthion)
p3 = [168,179]
p4 = [268,160]
#Left and Right eyes (Endocanthion to Endocanthion)
p5 = [290, 190]
p6 = [288, 218]
#Left eye (Exocanthion to endocanthion)
p7 = [220, 68]
p8 = [230, 100]
#Right eye (Exocanthion to endocanthion)
p9 = [219, 68]
p10 = [230, 100]
#Right eyebrow distance
p11 = [191,170]
p12 = [252,171]
#Left eyebrow Distance
p13 = [261, 185]
p14 = [276, 243]
#Upper Cheek (Zygion to Zygion)
p15 = [168, 179]
p16 = [324, 176]
#Nose Distance (Nasion to Alare)
p17 = [219, 68]
p18 = [230, 102]
#Mouth Distance (Pogonion to pogonion)
p19 = [205, 63]
p20 = [230, 102]
#Jawline Distance (Gonion to gonion)
p21 = [170,179]
p22 = [268,259]


distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
distance1 = math.sqrt( ((p3[0]-p4[0])**2)+((p3[1]-p4[1])**2) )
distance2 = math.sqrt( ((p5[0]-p6[0])**2)+((p5[1]-p6[1])**2) )
distance3 = math.sqrt( ((p7[0]-p8[0])**2)+((p7[1]-p8[1])**2) )
distance4 = math.sqrt( ((p9[0]-p10[0])**2)+((p9[1]-p10[1])**2) )
distance5 = math.sqrt( ((p11[0]-p12[0])**2)+((p11[1]-p12[1])**2) )
distance6 = math.sqrt( ((p13[0]-p14[0])**2)+((p13[1]-p14[1])**2) )
distance7 = math.sqrt( ((p15[0]-p16[0])**2)+((p15[1]-p16[1])**2) )
distance8 = math.sqrt( ((p17[0]-p18[0])**2)+((p17[1]-p18[1])**2) )
distance9 = math.sqrt( ((p19[0]-p20[0])**2)+((p19[1]-p20[1])**2) )
distance10 = math.sqrt( ((p21[0]-p22[0])**2)+((p21[1]-p22[1])**2) )

name="Forehead Distance                                                (Trichion to Glabella)(Tr-G):"
name1="Distance between External Points of Left and Right Eyes   (Exocanthion to Exocanthion)(ex-ex):"      
name2="Distance between Internal Points of Left and Right Eyes (Endocanthion to Endocanthion)(en-en):" 
name3="Width of Left Eye                            (Exocanthion to Endocanthion of Left Eye)(ex-en):" 
name4="Width of Right Eye                          (Exocanthion to Endocanthion of Right Eye)(ex-en):" 
name5="Width of Right Eyebrow                                                                       :" 
name6="Width of Left Eyebrow                                                                        :"
name7="Width of Middle Part of Face                    (Zygion to Zygion - Width of the Face)(zy-zy):" 
name8="Nose Distance                                                               (Nasion to Alare):" 
name9="Mouth Width                                     (Two End Points of Lips-Pogonion to Pogonion):" 
name10="Jawline Distance                                                           (Gonion to Gonion):" 

print(str(name),distance)
print(str(name1),distance1)
print(str(name2),distance2)
print(str(name3),distance3)
print(str(name4),distance4)
print(str(name5),distance5)
print(str(name6),distance6)
print(str(name7),distance7)
print(str(name8),distance8)
print(str(name9),distance9)
print(str(name10),distance10)
################################################################################
