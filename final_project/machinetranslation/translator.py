"""IBM TRANSLATOR"""

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

def english_to_french(english_text):
    """ Function To Translate English To French """
    while True:
        try:
            translation = language_translator.translate(english_text, model_id='en-fr').get_result()
            trans_list = translation["translations"]
            trans_dict = trans_list[0]
            french_text = trans_dict['translation']
            return french_text
        except ValueError:
            return None

def french_to_english(french_text):
    '''  Function To Translate FrenchToEnglish '''
    while True:
        try:
            translation = language_translator.translate(french_text, model_id='fr-en').get_result()
            trans_list = translation["translations"]
            trans_dict = trans_list[0]
            english_text = trans_dict['translation']
            return english_text
        except ValueError:
            return None

#print(englishToFrench('Hello'))
#print(frenchToEnglish('Bonjour'))
