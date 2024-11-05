# skin-infection-classification
The project aims to develop a neural network model capable of distinguishing between Ringworm and Pityriasis Rosea. These two skin conditions often appear similar, which leads to misdiagnosis, but they require different treatments. 

Dataset Collection
Images for both Ringworm and Pityriasis Rosea (PR) were collected using the [Image Downloader - Image Eye browser extension](https://tinyurl.com/image-down). This extension allows you to filter images by size and type, then download them into separate folders for each condition. One folder was created for Ringworm images, and another for Pityriasis Rosea images.

Data Preprocessing
Manual Cleaning: Since the dataset was relatively small, data cleaning was performed manually to remove irrelevant or poor-quality images.
Further Preprocessing:
Data Augmentation: Applied various augmentation techniques to increase the diversity of the training dataset.
Image Scaling: Images were scaled to meet the input requirements of the machine learning model.

Model Building
Transfer Learning: I used the Xception pre-trained model for transfer learning. This model was fine-tuned on the dataset to perform the classification task.
Model Training: The training process was conducted using Google Colab. You can find the code for training the model in the following notebook: https://tinyurl.com/skin-code

Model Deployment:
The trained model was deployed using Flask to create a web application for real-time skin infection classification.

Flask Deployment:
The Python file for the Flask application is app.py.
The HTML template for the web interface is located in the templates folder.
A sample test image is provided in the static folder for demonstration purposes.

Model and Training Data Download:
You can download the trained model and the training dataset from the following link: https://shorturl.at/GsOF0


Below is a screenshot showing the web interface of the deployed Flask application:
![image](https://github.com/user-attachments/assets/7e55af12-fea2-437e-ae79-5080ac8fbb5f)

