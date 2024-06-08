# Libraries
from tkinter import *
from PIL import Image, ImageTk
import imutils
import cv2
import numpy as np
from ultralytics import YOLO
import math

# Show Images
def images(img, imgtxt):
    img = img
    imgtxt = imgtxt

    # Image Detect
    img = np.array(img, dtype='uint8')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = Image.fromarray(img)

    img_ = ImageTk.PhotoImage(image=img)
    lblimg.configure(image=img_)
    lblimg.image = img_

    # Image Text
    imgtxt = np.array(imgtxt, dtype='uint8')
    imgtxt = cv2.cvtColor(imgtxt, cv2.COLOR_RGB2BGR)
    imgtxt = Image.fromarray(imgtxt)

    img_txt = ImageTk.PhotoImage(image=imgtxt)
    lblimgtxt.configure(image=img_txt)
    lblimgtxt.image = img_txt

# Scanning Function
def Scanning():

    global lblimg, lblimgtxt

    #Inferface
    lblimg = Label(pagina)
    lblimg.place(x=75, y=260)

    lblimgtxt = Label(pagina)
    lblimgtxt.place(x=995, y=310)

    # Read VideoCapture
    if cap is not None:
        ret, frame = cap.read()
        frame_show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if ret == True:

            results = model(frame, stream=True, verbose=False)
            for res in results:
                #Box
                boxes = res.boxes
                for box in boxes:
                    # Bonding Box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # Error
                    if x1 < 0: x1 = 0
                    if y1 < 0: y1 = 0
                    if x2 < 0: x2 = 0
                    if y2 < 0: y2 = 0

                    # Class
                    cls = int(box.cls[0])

                    #Confidence
                    conf = math.ceil(box.conf[0])


                    if conf > 0.5:

                        # Metal
                        if cls == 0:
                            # Draw Rectangle
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (224, 173, 0), 2)

                            # Text
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 1, 2)
                            dim = sizetext[0]
                            baseline = sizetext[1]
                            # Rectangle
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline), (224, 173, 0), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)

                            # Image
                            images(img_metal, img_metaltxt)

                        # Vidro
                        if cls == 1:
                            # Draw Rectangle
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (49, 140, 73), 2)

                            # Text
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 1, 2)
                            dim = sizetext[0]
                            baseline = sizetext[1]
                            # Rectangle
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline), (49, 140, 73), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)

                            # Image
                            images(img_vidro, img_vidrotxt)

                        # Plastico
                        if cls == 2:
                            # Draw Rectangle
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (203, 31, 27), 2)

                            # Text
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 1, 2)
                            dim = sizetext[0]
                            baseline = sizetext[1]
                            # Rectangle
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline), (203, 31, 27), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                            # Image
                            images(img_plastico, img_plasticotxt)

                        # Papel
                        if cls == 3:
                            # Draw Rectangle
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (48, 179, 162), 2)

                            # Text
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 1, 2)
                            dim = sizetext[0]
                            baseline = sizetext[1]
                            # Rectangle
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline), (48, 179, 162), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                            # Image
                            images(img_papel, img_papeltxt)

                        # Residuos Biologicos
                        if cls == 4:
                            # Draw Rectangle
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (186, 186, 186), 2)

                            # Text
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 1, 2)
                            dim = sizetext[0]
                            baseline = sizetext[1]
                            # Rectangle
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseline), (x1 + dim[0], y1 + baseline), (186, 186, 186), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                            # Image
                            images(img_hospital, img_hospitaltxt)

            # Resize
            frame_show = imutils.resize(frame_show, width=640)

            # Convert Video
            im = Image.fromarray(frame_show)
            img = ImageTk.PhotoImage(image=im)

            # Show
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, Scanning)

        else:
            cap.release()

# main
def pagina_principal():
    global model, clsName, img_metal, img_vidro, img_plastico, img_papel, img_hospital, lblVideo
    global img_metaltxt, img_vidrotxt, img_plasticotxt, img_papeltxt, img_hospitaltxt, cap, pagina

    #pagina principal
    pagina = Tk()
    pagina.title("ECOSCAN")
    pagina.geometry("1280x720")

    # Background
    imagemBG = PhotoImage(file="setUp/Canva.png")
    background = Label(image=imagemBG)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Modelo
    model = YOLO('Modelo/best.pt')

    # Classes
    clsName = ['Metal', 'Vidro', 'Plastico', 'Papel', 'Residuos Biologicos']

    # Imagens
    img_metal = cv2.imread("setUp/metal.png")
    img_vidro = cv2.imread("setUp/vidro.png")
    img_plastico = cv2.imread("setUp/plastico.png")
    img_papel = cv2.imread("setUp/papel.png")
    img_hospital = cv2.imread("setUp/hospitalar.png")

    img_metaltxt = cv2.imread("setUp/metaltxt.png")
    img_vidrotxt = cv2.imread("setUp/vidrotxt.png")
    img_plasticotxt = cv2.imread("setUp/plasticotxt.png")
    img_papeltxt = cv2.imread("setUp/papeltxt.png")
    img_hospitaltxt = cv2.imread("setUp/hospitalartxt.png")

    # Label Video
    lblVideo = Label(pagina)
    lblVideo.place(x=320,y=118)

    #Camera
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 640)
    cap.set(4, 480)

    # Scanning
    Scanning()

    # Loop
    pagina.mainloop()

if __name__ == '__main__':
    pagina_principal()


