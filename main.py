from PyPDF2 import PdfFileReader
from googletrans import Translator
import time
translator = Translator()

file = open("Bonsai.pdf", 'rb')
reader = PdfFileReader(file)
num_pages = reader.numPages

text_file = open(r"C:\Users\OperaCO\Downloads\plr/bonsai.txt", "w", encoding="utf-8")

for p in range(num_pages):
    time.sleep(3)
    page = reader.getPage(p)
    text = page.extractText()
    translate_text = translator.translate(text, dest='pt')

    # write string to file
    n = text_file.write(str(translate_text))
    print(n)

# fechar arquivo
text_file.close()
