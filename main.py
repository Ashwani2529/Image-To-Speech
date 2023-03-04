import pytesseract
from PIL import Image
from gtts import gTTS
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\91961\Downloads\TEI2S-master\terr\tesseract.exe'
src_path = './'
def get_string(img_path):
    result = pytesseract.image_to_string(Image.open(src_path + "3.png"))
    return result
img2txt = get_string(src_path + "3.png")
print('--- Recognizing text from image ---'+'\n'+img2txt)
myobj = gTTS(text=img2txt, lang='en', slow=False)
myobj.save('speech.mp3')
os.system('speech.mp3')