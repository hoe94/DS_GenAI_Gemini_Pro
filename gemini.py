import os
import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.environ['GOOGLE_API_KEY']
genai.configure(api_key = gemini_api_key)

'''List of the models from Gemini Pro'''
#for m in genai.list_models():
#    print(f'Model: {m.name}')
#    print(f'Supported_Methods: {m.supported_generation_methods}')
#    print('\n')


'''LLM from Gemini Pro'''
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Where is the Malaysia?')
print(response.text)
print(response.prompt_feedback)

'''LLM (Image) from Gemini Pro Vision'''
#img = PIL.Image.open('white-guy.jpg')
#img_model = genai.GenerativeModel('gemini-pro-vision')
#response2 = img_model.generate_content(img)
#print(response2.text)