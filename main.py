import pytesseract
from PIL import Image
from gtts import gTTS
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\91961\Downloads\TEI2S-master\terr\tesseract.exe'
directory_path = 'C:/Users/91961/Downloads/TEI2S-master/'
for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        with Image.open(file_path) as img:
                s=filename
                break
def get_string(img_path):
        result = pytesseract.image_to_string(Image.open(str(s)))
        return result
img2txt = get_string(str(s))
print('--- Recognizing text from image ---'+'\n'+img2txt)
myobj = gTTS(text=img2txt, lang='en', slow=False)
myobj.save('speech.mp3')
os.system('speech.mp3')
os.remove('speech.mp3')
