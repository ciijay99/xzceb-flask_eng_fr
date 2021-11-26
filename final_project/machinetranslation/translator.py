#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-09-15',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    translation = language_translator.translate(
        englishText,
        model_id='en-fr').get_result()
    trans_list = translation["translations"]
    trans_dict = trans_list[0]
    frenchText = trans_dict['translation']
    return frenchText

def frenchToEnglish(frenchText):
    while True:
        try:
            translation = language_translator.translate(
                frenchText, 
                model_id='fr-en').get_result()
            trans_list = translation["translations"]
            trans_dict = trans_list[0]
            englishText = trans_dict['translation']
            #print(json.dumps(translation, indent=2, ensure_ascii=False))
            return englishText
        except (ValueError):
            print("A value is required")
            break

#print(englishToFrench('Hello'))
#print(frenchToEnglish('Bonjour'))
