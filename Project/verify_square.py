import cv2

def square (img, op):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if op == 1:
        ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    else:
        ret, thresh = cv2.threshold(gray, 165, 255, cv2.THRESH_BINARY)

    cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find contours from mask

    #cv2.imshow ("gray", gray)
    #cv2.imshow ("thresh", thresh)

    approxWH = False
    for c in cnts:
        approx = cv2.approxPolyDP(c, 0.08 * cv2.arcLength(c, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(c)

            toleranta = 8  # Toleranța permisă între w și h

            if abs(w - h) <= toleranta:
                aproxWH = True
            else:
                aproxWH = False

            minWH = min(w, h)

            area = w * h
            if area >= 70000 and aproxWH == True:
                #print(area)
                start = (x, y)
                final = (x + minWH, y + minWH)
                img = cv2.rectangle(img, start, final, (255, 0, 0), 2)
                cv2.putText(img, "Big Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    return img, approxWH

def find_contour (img, color_name = "square"):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find contours from mask

    for c in cnts:
        approx = cv2.approxPolyDP(c, 0.08 * cv2.arcLength(c, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(c)
            area = w * h

            toleranta = 50  # Toleranța permisă între w și h

            if abs(w - h) <= toleranta:
                aproxWH = True
            else:
                aproxWH = False
            if area >= 1700 and aproxWH == True:
                start = (x, y)
                final = (x + w, y + h)
                img = cv2.rectangle(img, start, final, (255, 0, 0), 2)
                cv2.putText(img, color_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    return img
