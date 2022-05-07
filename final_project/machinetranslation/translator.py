import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']





authenticator = IAMAuthenticator('xyaWAkpv3pahmG9nivvwzJJ3wz1uhIQ0YObd3wRXgxuU')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/01f0efa0-e4ff-4157-8f67-2ccb20b72d9c')



def englishToFrench(englishText):
    frenchTextU = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    frenchText=frenchTextU.get('translations')[0].get('translation')
    
    return frenchText



def frenchToEnglish(frenchText):
    englishTextU = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    frenchText=englishTextU.get('translations')[0].get('translation')
    
    return frenchText






