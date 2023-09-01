import cv2

# coordonate de start si final patrat alb gol
start_point_square = (150, 100)
end_point_square = (450, 400)

def add_banner(img, start_point, end_point):

    #variabile dreptunghi alb plin
    rectangle_color = (255, 255, 255)
    thickness = -1

    cv2.rectangle(img, start_point, end_point, rectangle_color, thickness)

    return img

def add_text (img, txt, coordinates):
    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 0.5
    txt_color = (0, 0, 0)
    thickness = 1

    cv2.putText(img, txt, coordinates, font, fontScale, txt_color, thickness, cv2.LINE_AA)

    return img

def add_indications(img, text):
    # coordonate text
    coordinates = (25, 25)

    # coordonate de start si final banner alb
    start_point = (0, 0)
    end_point = (640, 50)

    img = add_banner(img, start_point, end_point)
    img = add_text(img, text, coordinates)

    return img

def add_rectangle (img, start_point, end_point):
    rectangle_color = (255, 255, 255)
    thickness = 3

    cv2.rectangle(img, start_point, end_point, rectangle_color, thickness)

    return img

def crop_image (img, start_point, end_point):
    img = img[start_point[1]:end_point[1], start_point[0]:end_point[0]]

    return img