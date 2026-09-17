import cv2
import numpy as np

img = cv2.imread("assets/foto_terang.jpg")
img2 = cv2.imread("assets/kontras_rendah.jpg")
kontras_rendah_resize = cv2.resize(img2, (600, 400))

# transformasi intensitas
def negative_image(image):
    h, w, c = image.shape

    hasil = image.copy()

    for i in range(h):
        for j in range(w):
            for c in range(3):
                hasil[i, j, c] = 255 - image[i, j, c]

    cv2.imshow("Foto Asli", img)
    cv2.imshow("Negative", hasil)

    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
negative_image(img)






