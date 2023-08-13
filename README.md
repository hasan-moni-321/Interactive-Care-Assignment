# Interactive-Care-Assignment  

##   About Files
1. input_data folder carrying some pdf file for testing with script.py file 
2. categorized_resume.csv file is the generated file after running the script.py file
3. english_stopwords.txt file for cleaning the dataset
4. resume_classification.ipynb file for loading data, cleaning data, Exploratory Data Analysis, feature engineering, model building, model training, model analysis, model testing, model downloading etc.    
5. script.py file is the main file for running.


##   Everything I did in my Linux(Ubuntu 22.04) Operating System. I used terminal for running script.py file    

##   Steps of running script.py file 

Step-1:   Make a directory in your local computer. use below command for making directory.   
mkdir myproject 


Step-2: got to the myproject directory. Use below command to go to myproject directory.   
cd myproject 


Step-3:   Clone the repository. Use below code for cloning the repository.     
git clone https://github.com/hasan-moni-321/Interactive-Care-Assignment


Step-4:   Got to the Interactive-Care-Assignment folder using below command.  
cd Interactive-Care-Assignment


Step-5:   Download the trained model from the below link. 
https://drive.google.com/drive/u/0/folders/1ZVC4RkzsSuROPVVsoNWJy8AjyN43CGCA


Step-6: keep the downloaded model in the Interactive-Care-Assignment directory. Don't change the model name! 


Step-7: install framework and libraries. Run below command in your terminal one by one.  
pip install numpy   
pip install pandas   
pip install PyPDF2    
pip install aspose-pdf   
pip install nltk   
pip install tensorflow   


Step-8: Run the script.py file using below command.   
python script.py


Step-9:  Check! A directory named output_data should create in the myproject folder. Where pdf file will generated in categorized folder. And Categorized_resume.csv file will generated.    



Note: model size is 433.9 MB. That is large size of model. For that I kept the model in my Google Drive. I used only 15 pdf files for running script.py file. Those 15 pdf file are located in the input_data directory. 
