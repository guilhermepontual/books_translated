from googletrans import Translator
translator = Translator()

teste = translator.translate('This is so nice!', src='en', dest='fr').text
print(teste)
