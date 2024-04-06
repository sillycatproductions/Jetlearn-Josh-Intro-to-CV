import cv2
image = cv2.imread('pikachu.png',1)
B,G,R = cv2.split(image)

cv2.imshow('PIKACHU PARTYYYY', image)
cv2.waitKey(delay = 5000)
cv2.destroyWindow('PIKACHU PARTYYYY')

cv2.imshow('BLUE', B)
cv2.waitKey(delay = 5000)
cv2.destroyWindow('BLUE')

cv2.imshow('GREEN', G)
cv2.waitKey(delay = 5000)
cv2.destroyWindow('GREEN')

cv2.imshow('RED', R)
cv2.waitKey(delay = 5000)
cv2.destroyWindow('RED')