import cv2
import verify_square as sq
import select_color as sc
import take_photo as tp

def main():
    # citire img
    tp.six_faces()

    #identificare patrat
    for i in range (6):
        img_path = "image{}.png".format(i)
        img = cv2.imread(img_path)
        #cv2.imshow("img", img)
        sqr_img, ans = sq.square(img, 1)
        if ans == False:
            sqr_img, ans = sq.square(img, 2)

        # identificare si clasare culori
        hsv = cv2.cvtColor(sqr_img, cv2.COLOR_BGR2HSV)  # convertion to HSV
        for name, clr in sc.colors.items():  # for each color in colors
            curr_color_img = sc.find_color(sqr_img, hsv, clr, name)
            if (name == 'blue'):
                result = curr_color_img
            else:
                result = cv2.add(result, curr_color_img)

        cv2.imshow("met 2", result)
        cv2.imwrite("color_det_image{}.png".format(i), result)

    cv2.waitKey (0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

# de facut: fiecare masca sa identifice culorile si contururile si dupa sa unesc toate cele 5 masti
# yolo de facut