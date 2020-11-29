#need to install pyttsx3 library for texttospeech conversion,
#and also install PyPDF2 for extracting information of pdf file
import pyttsx3
import PyPDF2

pdf=open("insbook.pdf", "rb") #you will be give your own pdf that you want to listen
pdfreader=PyPDF2.PdfFileReader(pdf)
pages=pdfreader.numPages
print(pages)

speaker=pyttsx3.init()
startpage=pdfreader.getPage(29)
text=startpage.extractText()
speaker.say(text)
speaker.runAndWait()
