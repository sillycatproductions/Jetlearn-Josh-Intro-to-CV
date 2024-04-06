import cv2

img = cv2.imread('pikachu.png',0)

# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color. excludes transaperency
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

cv2.imshow('Pikachu Image',img) #'imshow' helps load the image ina a new window and gives it a title (the quotation 'Pikachu Image')

cv2.waitKey(0) #helps keep the window until the keyboard is pressed

cv2.destroyAllWindows() #helps delete the window when a key is pressed