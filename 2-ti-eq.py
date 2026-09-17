import cv2
import numpy as np

img = cv2.imread("assets/foto_terang.jpg", cv2.COLOR_BGR2GRAY)

img2 = cv2.imread("assets/kontras_rendah.jpg")
kontras_rendah_resize = cv2.resize(img2, (600, 400))

img3 = cv2.imread("assets/foto_gelap.jpg")
foto_gelap_resize = cv2.resize(img3, (600, 800))


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
# negative_image(img)

def ekualisasi_histogram(image):
    img_to_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    h, w = img_to_grayscale.shape
    total_pixels = h * w

    histogram = np.zeros(256, dtype=int)

    for i in range(h):
        for j in range(w):
            intensity = img_to_grayscale[i, j]
            histogram[intensity] += 1

    cdf = np.zeros(256, dtype=int)
    current_sum = 0

    for i in range(256):
        current_sum += histogram[i]
        cdf[i] = current_sum

    cdf_min = np.min(cdf[cdf > 0])
    equalized_lookup_table = np.zeros(256, dtype=np.uint8)

    for i in range(256):
        if cdf[i] == 0:
            equalized_lookup_table[i] = 0
        else:
            numerator = cdf[i] - cdf_min
            denominator = total_pixels - cdf_min

            if denominator == 0:
                equalized_lookup_table[i] = 0
            else:
                equalized_lookup_table[i] = np.uint8(
                    round((numerator / denominator) * 255)
                )

    img_equalized = np.zeros_like(img_to_grayscale)

    for i in range(h):
        for j in range(w):
            img_equalized[i, j] = equalized_lookup_table[img_to_grayscale[i, j]]

    cv2.imshow("Foto Asli", image)
    cv2.imshow("Foto Grayscale", img_to_grayscale)
    cv2.imshow("Foto Equalized", img_equalized)

    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()

ekualisasi_histogram(kontras_rendah_resize)




