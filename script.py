#import necessary libraries
import numpy as np 
import pandas as pd 

from PyPDF2 import PdfReader
import aspose.pdf as ap
import shutil

import re, string, os 

import nltk 
from nltk.tokenize import word_tokenize

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


# define nltk stemmer 
stemmer = nltk.stem.porter.PorterStemmer()
tokenizer = Tokenizer(num_words=120000) 

# Loading english stop words file
with open('./english_stopwords.txt', 'r', encoding='utf-8-sig') as f:
    stop_word = f.read() 
    stop_word = stop_word.replace(" ", "")
    stop_word = stop_word.split('\n')
    #print(stop_word)

def clean_dataset(txt): 
    txt = txt.lower() 
    txt = re.sub('[^a-zA-Z]', ' ', txt)
    #txt = word_tokenize(txt)
    txt = txt.split() 
    #txt = [w for w in txt if not w in nltk.corpus.stopwords.words('english')]
    txt = [w for w in txt if not w in stop_word] 
    txt = [stemmer.stem(w) for w in txt]
    return ' '.join(txt)


def reading_multiple_pdf_file(main_path, model, encode_dict):
     # making a directory 
     output_dir_path = "./output_data"
     if os.path.exists(output_dir_path): 
          shutil.rmtree(output_dir_path) 
     os.mkdir(output_dir_path)  
     # a dictionary for creating csv file 
     data_dict = {"filename": [], "category": [] } 

     resume_categories = os.listdir(main_path)
     #print(resume_categories) 
     for cate in resume_categories:
          resume_cate_path = os.path.join(main_path, cate)  
          resume_pdf_list = os.listdir(resume_cate_path)

          for pdf in resume_pdf_list:
               str = '' 
               resume_full_path = os.path.join(resume_cate_path, pdf)

               # Reading pdf
               reader = PdfReader(resume_full_path) 
               pdf_page_length = len(reader.pages) 
               for pag in range(0, pdf_page_length): 
                    page = reader.pages[pag]  
                    text = page.extract_text() 
                    str += text 
               
               # data cleaning  
               text = clean_dataset(str)
               # Tokenizer and pad sequence 
               text_token = tokenizer.texts_to_sequences([text]) 
               text_pad = pad_sequences(text_token, padding='post', maxlen=250)
               # predict with ML model
               prediction = model.predict(text_pad) 
               prediction = np.rint(prediction)
               prediction = np.argmax(prediction, axis=1) 
               result = list(encode_dict.keys())[list(encode_dict.values()).index(prediction[0])]

                    
               # making dictionary for csv file 
               data_dict['filename'].append(pdf) 
               data_dict['category'].append(result)   

               # making pdf file for saving in a folder 
               document = ap.Document() 
               page = document.pages.add() 
               text = ap.text.TextFragment(str) 
               page.paragraphs.add(text)

               #pdf_path = 
               if not os.path.exists(os.path.join("./output_data/", result)): 
                    os.mkdir(os.path.join("./output_data", result))
            #    else:
            #         document.save(os.path.join("./output_data", result, pdf))  
               
          str = "" 
     # making csv file. Save csv file into directory
     df = pd.DataFrame(data_dict)
     df.to_csv("./output_data/categorized_resume.csv", index=False)
     return df  


       
encode_dict = {"accountant":0, "advocate":1, "agriculture":2, "apparel":3, "arts":4, "automobile":5, "aviation":6, "banking":7, "bpo":8, "businessdevelopment":9, "chef":10, "construction":11, "consultant":12, "designer":13, "digitalmedia":14, "engineering":15, "finance":16, "fitness":17, "healthcare":18, "hr":19, "informationtechnology":20, "publicrelations":21, "sales":22, "teacher":23} 
loaded_model = load_model("./resume_classification_deep_learning_1.h5")      

pdf_main_path = "./input_data/"
df = reading_multiple_pdf_file(pdf_main_path, loaded_model, encode_dict) 

