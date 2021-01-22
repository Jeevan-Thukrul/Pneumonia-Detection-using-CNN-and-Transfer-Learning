# Pneumonia-Detection-using-CNN-and-Transfer-Learning

## Project overview
- To develop an Intelligent System that receives an X-ray image of the lungs as an input and based on the processed image it predicts the probability of a person having pneumonia as an output using Deep Learning and Transfer Learning.

## App Output
![alt text](Output/output.gif)


## Training and Testing Accurcy (CNN)
- Train accuracy: 0.9534
- Test accuracy: 0.9102 </br>
![alt text](https://github.com/Jeevan-Thukrul/Pneumonia-Detection-using-CNN-and-Transfer-Learning/blob/master/Output/cnn_acc.png)

## Training and Testing Loss (CNN)
- Train loss: 0.1288
- Test loss: 0.2562 </br>
![alt text](https://github.com/Jeevan-Thukrul/Pneumonia-Detection-using-CNN-and-Transfer-Learning/blob/master/Output/cnn_loss.png)

## Training and Testing Accurcy (Transfer Learning)
- Train accuracy: 0.9385
- Test accuracy: 0.8958 </br>
![alt text](https://github.com/Jeevan-Thukrul/Pneumonia-Detection-using-CNN-and-Transfer-Learning/blob/master/Output/tl_acc.png)

## Training and Testing Loss (Transfer Learning)
- Train loss: 0.1643
- Test loss: 0.2839 </br>
![alt text](https://github.com/Jeevan-Thukrul/Pneumonia-Detection-using-CNN-and-Transfer-Learning/blob/master/Output/tl_loss.png)


## Folders and Files Description

### Output
- Contains the App's final output 

### Pneumonia Detection.ipynb
- It is the python notebook used to preprocess the data and to build, train and save the model.

## Files for our Streamlit App

#### classify.py
- get_model(): Loads the saved model into cache using streamlit's "@st.cache" feature.
- predict(): Takes an image as input from the function parameter, preprocesses it and feeds it to the model for results.

#### app.py
- Contains the front-end code for the streamlit app.
- Imports the predict() function fetches the result and displays it.

### To run it on your system
- Install all the dependencies
- Clone this repository
- You need the Streamlit App folder to run this application.
- In your Command line/Terminal go to the directory file then type
 
```
 streamlit run app.py
```
