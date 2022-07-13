

from flask import Flask, render_template, request
from keras.models import load_model
#from keras.preprocessing import image
from keras.utils import image_utils as image
import numpy as np


def func(path):
  img = image.load_img(path,target_size=(224,224))

  i=image.img_to_array(img)/255
  input_arr = np.array([i])
  input_arr.shape


  pred1=(model.predict(input_arr))
  print (pred1)
  a= 1-pred1

  if (a<pred1):
    msg = "T.B. Positive"
  else:
    msg = "T.B. Negative"

  return msg

app = Flask(__name__)
# run_with_ngrok(app)

model=load_model('finalmodel.h5')

@app.route("/")
def index():
	return(render_template("index.html"))
 

 
@app.route("/predict", methods = ['POST'])
def predict():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)
  
		p = func(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0')

# ngrok.kill()
