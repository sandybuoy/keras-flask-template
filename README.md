# keras-flask-template
A template structure for Deep Learning Models that are implemented using Keras API.  
This project focuses on how easy you design, configure, test and later on deploy your own model in an easier fashion.  
For deployment Flask API is used to get predictions by providing inputs from the browser.  
  
As the model training starts, several logs are generated to keep track of the performance of the model and a summary is saved in the end which will keep hold of different model trained.  

In the end, the user has the option to choose a saved model that can be ustilized by the flask server for the prediction.  

## Note:  
####  The execution starts from mains>example.py (With CatDog Example).  
####  Model can be selected for deployment by running utils>choose_model.py
####  Finally, the Flask server can be started by running deploy_model>API.py
