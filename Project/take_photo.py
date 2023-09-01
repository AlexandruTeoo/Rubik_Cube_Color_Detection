import cv2
import time
import modify_img as modify

# Funcție pentru a captura o imagine cu camera web și a o afișa în timp real
def capture_image(photo_count, msg):
    # Deschide camera web
    cap = cv2.VideoCapture(0)

    # Așteaptă 2 secunde pentru a permite camerei web să se calibreze
    time.sleep(2)

    start_time = time.time()

    while True:
        # Citirea unei cadre din camera web
        _, img = cap.read()

        # Afișează imaginea într-o fereastră
        cv2.imshow("Imagine in timp real", img)
        modify_img = img.copy()

        modify_img = modify.add_rectangle(modify_img, modify.start_point_square, modify.end_point_square)
        modify_img = modify.add_indications(modify_img, msg)
        cv2.imshow("crop img", modify_img)
        cv2.imshow("Imagine in timp real 2", img)
        sqr_img = modify.crop_image(img, modify.start_point_square, modify.end_point_square)

        # Verifică timpul pentru a decide când să faci poza
        current_time = time.time()
        if current_time - start_time >= 5:
            # Capturează imaginea
            cv2.imwrite("image{}.png".format(photo_count), sqr_img)
            print("Poza {} a fost realizată".format(photo_count))

            # Oprire afișare în timp real pentru a afișa mesajul de așteptare
            cv2.destroyAllWindows()
            break

        # Așteaptă 1 ms și verifică dacă a fost apăsată tasta 'q' pentru a închide fereastra
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Închide camera web
    cap.release()

def six_faces ():
    # Realizează cele 6 poze
    for i in range(6):
        # Afișează mesajul pentru poziția dorită
        if i == 0:
            msg = "Rotiți obiectul in sus"
        elif i == 1:
            msg = "Rotiți obiectul in jos"
        elif i == 2:
            msg = "Rotiți obiectul in stanga"
        elif i == 3:
            msg = "Rotiți obiectul in dreapta"
        elif i == 4:
            msg = "Rotiți obiectul in sus"
        elif i == 5:
            msg = "Rotiți obiectul in jos"
        print (msg)

        # img = modify.add_rectangle(img, modify.start_point_square, modify.end_point_square)
        # cv2.imshow("img", img)
        # sqr_img = modify.crop_image(img, modify.start_point_square, modify.end_point_square)
        capture_image(i, msg)