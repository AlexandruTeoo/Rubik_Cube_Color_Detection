import cv2
import time

# Deschide camera web
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 420)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 420)

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

# Funcție pentru a captura o imagine cu camera web și a o afișa în timp real
def capture_and_show_live_image(i, txt):
    # Inițializare variabile
    start_time = time.time()

    # coordonate de start si final patrat alb gol
    start_point_square = (150, 100)
    end_point_square = (450, 400)

    # Așteaptă 1 secunde pentru a permite camerei web să se calibreze
    time.sleep(1)

    while True:
        # Citirea unei cadru din camera web
        ret, frame = cam.read()

        original_img = frame.copy()
        frame = add_indications(frame, txt)

        frame = add_rectangle (frame, start_point_square, end_point_square)

        # Afișează imaginea într-o fereastră
        cv2.imshow("Cub Rubik", frame)
        current_time = time.time()

        crop_img = crop_image(original_img, start_point_square, end_point_square)

        if current_time - start_time >= 5:
            # Capturează imaginea
            cv2.imwrite("image_test{}.png".format(i+1), crop_img)
            print("Poza {} a fost realizată".format(i+1))
            break
        # Așteaptă 1 ms și verifică dacă a fost apăsată tasta 'q' pentru a închide fereastra
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Realizează cele 6 poze
for i in range(6):
    # Afișează mesajul pentru poziția dorită
    txt = "Se va face poza la partea cubului amplasata in "
    if i == 0:
        message = txt + "fata"
        print(message)
    elif i == 1:
        message = txt + "stanga"
        print(message)
    elif i == 2:
        message = txt + "spate"
        print(message)
    elif i == 3:
        message = txt + "dreapta"
        print(message)
    elif i == 4:
        message = txt + "sus"
        print(message)
    elif i == 5:
        message = txt + "jos"
        print(message)

    capture_and_show_live_image(i, message)

print("Procesul de capturare a imaginilor a fost finalizat.")

# Închide camera web
cam.release()
cv2.destroyAllWindows()