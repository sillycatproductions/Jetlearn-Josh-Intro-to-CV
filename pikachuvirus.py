import cv2 
import os

img = cv2.imread('pikachu.png',1)
cv2.imshow('Pikachu!', img)

#changes the path to where you wish to save the image
path = 'D:/Open CV/Lesson 1' 

#changes directory to what the function 'path' has saved
os.chdir(path)

#writes the file into the function 'path'
for i in range(5):
    cv2.imwrite(str(i + 1)+'.png',img)
print('Your files are getting flooded with pikachu!')

#delete the window
cv2.waitKey(delay = 5000)
cv2.destroyAllWindows()