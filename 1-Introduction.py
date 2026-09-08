import cv2
import numpy as np

image_path = {
"foto_gelap": "assets/foto_gelap.jpg",
"foto_terang": "assets/foto_terang.jpg",
"kontras_rendah": "assets/kontras_rendah.jpg"
}

FOTO_GELAP = cv2.imread(image_path["foto_gelap"])
FOTO_TERANG = cv2.imread(image_path["foto_terang"])
KONTRAS_RENDAH = cv2.imread(image_path["kontras_rendah"])

kontras_rendah_resize = cv2.resize(KONTRAS_RENDAH, (600, 400))
foto_gelap_resize = cv2.resize(FOTO_GELAP, (600, 800))

loaded_images = {
    # "foto_gelap": foto_gelap_resize,
    "foto_terang": FOTO_TERANG,
    # "kontras_rendah": kontras_rendah_resize
}

def showImageProperties():
    [h,w,c] = FOTO_TERANG.shape

    # Image filter (channel itu dari 0,1,2) untuk BGR
    for i in range(h):
        for j in range(w):
                       #x,y,c
            FOTO_TERANG[i,j,1] = 0
            FOTO_TERANG[i,j,2] = 0

    for name, image in loaded_images.items():

        cv2.imshow(name, image)

        print(f"{name}: {image.shape}, {image.dtype}, min: {image.min()}, max: {image.max()}, mean: {image.mean()}")
        print(f"{name}: {image}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# showImageProperties()


def liveCamFeed():
    capture = cv2.VideoCapture(0)

    while True:
        bool, frame = capture.read()

        cv2.imshow("Live Cam Feed", frame)

        if cv2.waitKey(1) == ord('q'):
            break
liveCamFeed()