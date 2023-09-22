from PIL import Image
from pytesseract import pytesseract
import enum

class OS(enum.Enum):
    Mac = 0
    Windows = 1
class language(enum.Enum):
    Eng = "eng"


class ImageReader:

    def __init__(self,os: OS):
        if os == OS.Mac:
            print("Running on Mac\n")
            #the above thing is running on mac via homebrew
        if os == OS.Windows:
            path = "testing"
            #exe file
    def extract_text(self,image:str, lang: str) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        return extracted_text
if __name__ == "__main__":
    ir = ImageReader(OS.Mac)
    text = ir.extract_text('/Users/kumartanay/Downloads/a1f88733921c820db477d054fe96afbb.jpg', lang='eng')
    print(text)






