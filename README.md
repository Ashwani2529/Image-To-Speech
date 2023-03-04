# TEI2S

## About
TEI2S (Text Embedded Image to Speech conversion) is a project which is really helpful for the visually impaired, in a sense that it takes an image containing text embedding as the input, extracts the text from the image, and converts this text to speech, i.e; the output is an audio file containing the text which is embedded in the provided input image.

## Configuration Steps
1. Cloning the repository

```
$ git clone https://github.com/Ashwani2529/Image-To-Speech.git
```

2. Installing the dependencies

First goto the (https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.0.20221222.exe) engine, and then extract the .exe file in folder named "terr" read the steps and install it on your system. After installing it, follow the steps mentioned below.

```
$ pip install numpy

$ pip install PIL

$ pip install opencv-python

$ pip install pytesseract

$ pip install gTTS
```
This installs all the required dependencies like Numpy, PIL (Python Imaging Library), OpenCV, Pytesseract and gTTS.

3. Running the file

Open the terminal and `cd` to the directory where you have cloned the repository. Then run the file by typing `python main.py`.
