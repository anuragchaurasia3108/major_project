import PyPDF2

import speech_recognition as sr
import pyttsx3
import googletrans
import gtts
import playsound
import os

r = sr.Recognizer()
translator = googletrans.Translator()
print(googletrans.LANGUAGES)
input_lang = 'en'
output_lang = 'hi'


def SpeakText(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()


while (1):
	try:
		print("Now say as your wish...")
		# with sr.Microphone() as source2:
		# 	r.adjust_for_ambient_noise(source2)
		# 	audio2 = r.listen(source2)
		# 	MyText = r.recognize_google(audio2, language=input_lang)
		# 	MyText = MyText.lower()

		book = open('ms-17.pdf', 'rb')
		pdfReader = PyPDF2.PdfFileReader(book)
		pages = pdfReader.numPages
		print(pages)
		speaker = pyttsx3.init()
		# for num in range(1, pages):
		page = pdfReader.getPage(2)
		print(page)
		MyText = page.extractText()
		print(MyText)
		# speaker.say(text)
		# speaker.runAndWait()
		# print("Did you say:- " + MyText)
		translated = translator.translate(MyText, dest=output_lang)
		print(translated.text)
		# SpeakText(MyText)
		converted_audio = gtts.gTTS(translated.text, lang=output_lang)
		converted_audio.save('textt.mp3')
		playsound.playsound('textt.mp3')
	# os.system('start aa.mp3')
	# with open(str(aa), 'wb') as f:
	# 	converted.save('aa.mp3')
	# 	playsound.playsound('aa.mp3')

	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))

	except sr.UnknownValueError:
		print("unknown error occured")


