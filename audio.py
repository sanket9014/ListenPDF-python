import pyttsx3
import PyPDF2

pdf=open("insbook.pdf", "rb")
pdfreader=PyPDF2.PdfFileReader(pdf)
pages=pdfreader.numPages
print(pages)

speaker=pyttsx3.init()
startpage=pdfreader.getPage(29)
text=startpage.extractText()
speaker.say(text)
speaker.runAndWait()