import cv2
import numpy as np
import pytesseract
from PIL import Image
from gtts import gTTS
import os
import subprocess
subprocess.Popen('start microsoft.windows.camera:', shell=True)
input()
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\91961\Downloads\TEI2S-master\terr\tesseract.exe'
src_path = './'
for filename in os.listdir(src_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith("Pro"):
        new= "2.jpg"
        os.rename(os.path.join(src_path, filename), os.path.join(src_path, new))
def get_string(img_path):
    img = cv2.imread(img_path)
    img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(src_path + "2.jpg", img)
    result = pytesseract.image_to_string(Image.open(src_path + "2.jpg"))
    return result
print('--- Recognizing text from image ---')
img2txt = get_string(src_path+"2.jpg")
print(img2txt)
myobj = gTTS(text=img2txt, lang='en', slow=False)
myobj.save('output1.mp3')
os.system('output1.mp3')
os.remove('2.jpg')
os.remove('output1.mp3')
