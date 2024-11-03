# skin-disease-classification
This project aims to create a model to distinguish between ringworm and pityriasis rosea. Pityriasis rosea is often misdiagnosed as ringworm because they look very familiar but they require different treatments.


The steps taken to build the model include:
Pityriasis rosea(PR) and ringworm images were downladed using the image downloader-image eye extension. Here's the link to install the extension:https://chromewebstore.google.com/detail/image-downloader-imageye/agionbommeaifngbhincahgmoflcikhm?hl=en-US&pli=1
The extension allows you to filter images by size and filter type and downloads the images in a folder. One folder for ringworm searches and one for PR


Data cleaning was done manually since the images were not a lot and the extension helped with filtering
I used google collab for my code file. I imported the images from my data directory using the tf.keras library

Further preprocessing were carried out on the images; data augmentation, scaling to match model input requirements
I applied transfer learning using the Xception pretrained model
Model was deployed on flask 
