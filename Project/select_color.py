import cv2
import numpy as np
import verify_square as sq

color = (255,255,255)
# I have defined lower and upper boundaries for each color for my camera
# Strongly recommended finding for your own camera.
colors = {'blue': [np.array([100, 160, 100]), np.array([160, 255, 255])],
          'red': [np.array([164, 91, 142]), np.array([181, 255, 255])],
          'yellow': [np.array([23, 50, 120]), np.array([40, 255, 255])],
          'green': [np.array([52, 50, 99]), np.array([95, 255, 255])],
          'orange': [np.array([0, 130, 120]), np.array([16, 255, 255])]}

def find_color(img, hsv, points, name):
    mask = cv2.inRange(hsv, points[0], points[1])  # create mask with boundaries
    final = cv2.bitwise_and(img, img, mask=mask)
    final = sq.find_contour(final, name)
    return final

def select_color (color):
    # Verificarea în ce categorie se încadrează culoarea
    for name, (lower, upper) in colors.items():
        if np.all(lower <= color) and np.all(color <= upper):
            return name

    return "?"