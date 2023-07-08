# Leaf Disease Detection Web Application

 This application has been implemented for my Bachelor Thesis which was centered around leaf disease detection using convolutional neural networks. The aim of this thesis was to make a comparison between different approaches. I've implemented three different models, one that employed a transfer learning approach using the InceptionV3 architecture, one that combined transfer learning with multi-task learning, and one that I've implemented myself using 3 convolutional layers. 
 
The app was written with FastAPI and React. It consists of only one page, where the user can upload a picture with leaves and selects the model he wants to be used for the prediction. Upon submiting, the request is sent via a POST call to the FastAPI server, which processes it and then sends the response containing the predictions to the React app, which then shows it to the end user using 2 charts, one for the plant species and one for the detected diseases.

![mainpage](https://github.com/GeorgeDanicico/Leaf-Disease-Detection/assets/72121511/ce3236e3-59bc-4e00-bde0-c5341db1e5d9)
![modelselect](https://github.com/GeorgeDanicico/Leaf-Disease-Detection/assets/72121511/81dbb997-9212-4718-b911-f86655c4d496)
![seeprediction](https://github.com/GeorgeDanicico/Leaf-Disease-Detection/assets/72121511/d665815e-d87b-4834-8d04-dc6c22560480)
