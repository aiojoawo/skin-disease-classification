from flask import Flask, render_template,request
import tensorflow as tf
from keras_preprocessing.image import load_img, img_to_array

import numpy as np

app = Flask(__name__)

#load model
reloaded =tf.keras.layers.TFSMLayer("model.pb")


#model._make_predict_function()

#define class names
dic=['pityriasis rosea', 'ringworm']


#define function to predict label
def predict_label(img_path):
    i = load_img(img_path, target_size=(256,256))
    x=img_to_array(i)
    x=np.expand_dims(x,axis =0)
    logits=reloaded(x)
    label_index=np.where(logits.numpy()>0.5,1,0)
    label = dic[label_index[0][0]]
    return label


#Define routes
@app.route("/", methods=['GET','POST'])
def main():
    return render_template("index.html")

@app.route("/submit", methods=["GET","POST"])
def get_hours():
    if request.method =='POST':
        img = request.files['my_image']
        
        img_path = "static/" + img.filename
        img.save(img_path)

        label = predict_label(img_path)
        p=label
    return render_template("index.html", prediction = p,img_path=img_path)




if __name__ =='__main__':
	
	app.run(debug = True,use_reloader=False)