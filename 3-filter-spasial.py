import cv2
import numpy as np

img = cv2.imread("assets/foto_gelap.jpg", cv2.IMREAD_GRAYSCALE)
foto_gelap_resize = cv2.resize(img, (600, 800))

h, w = foto_gelap_resize.shape
img_blur = np.zeros((h, w), dtype=np.uint8)

kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

for i in range(1, h - 1):
    for j in range(1, w - 1):
        total = 0

        for k in range(-1, 2):
            for l in range(-1, 2):
                total += int(foto_gelap_resize[i + k, j + l]) * kernel[k + 1, l + 1]

        img_blur[i, j] = total // 16

cv2.imshow("Foto Asli", foto_gelap_resize)
cv2.imshow("Gaussian Blur", img_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()