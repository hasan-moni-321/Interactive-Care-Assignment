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
https://drive.google.com/file/d/14t0c-ziQ2_V_rhbGvFoeAlLITYMjhp8h/view?usp=sharing


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

##   How to Increase Accuracy  
1. Increase the number of meaningful data.
2. Drop the Outlier (I didn't drop the outlier because of the small dataset).
3. Drop the Duplicate data (I didn't drop duplicate data because of the small dataset).
4. Test with Different Classification Machine Learning Model and Choose the best one for example T5 pretrained model, BERT
5. Use Skopt, Optuna Libraries for Hyperparameter Tuning.
6. Increase the Number of Features and choose the most correlated features for training.
7. Use Tensorflow Keras Tuner for Hyperparameter Tuning of Deep Neural Network.

## Limitation of this Project 

1. Scarcity of the meaningful data in the dataset  
2. Short time (given dataset is messy data. Need more and more time for best feature engineering)  



Note: model size is 433.9 MB. That is large size of model. For that I kept the model in my Google Drive. I used only 15 pdf files for running script.py file. Those 15 pdf file are located in the input_data directory.  


