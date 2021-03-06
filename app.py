from flask import Flask,render_template,redirect,request
import Color_Extraction_Flask
import cv2
import os
import numpy as np
from PIL import Image  
import PIL
# import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def color():
	return render_template("index.html")

@app.route("/",methods=["POST"])
def image():
	if request.method == "POST":
		n = request.form["k_value"]
		k = int(n)
		# print(k)
		f = request.files["userfile"]
		path = "./static/{}".format(f.filename) 
		f.save(path)
		# print(f.filename[-4:])

		new_img = Color_Extraction_Flask.change_color(path,k)
		new_img = np.array(new_img)
		new_img = Image.fromarray(new_img.astype('uint8'))
		# print(f.filename[-4])
		# if len(f.filename[:-4])>3
		if f.filename[-4]=='.':
			generated_result = f.filename[:-4] + "_1" + f.filename[-4:]
		else:
			generated_result = f.filename[:-5] + "_1" + f.filename[-5:]
		
		new_img.save(os.path.join('./static/',generated_result))
		# new_img.save('./static/')
		# new_img = np.array(new_img)
		# new_img=new_img[:,:,::-1]
		# new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)
		# cv2.imwrite("./static_filter/{}".format(f.filename), new_img)
		# cv2.imwrite(os.path.join('./static_filter',f.filename), new_img)

		# new_path = './static/'
		new_path = os.path.join('./static/',generated_result)

		result_dic = {"path":path,"new_path":new_path}

	return render_template("index.html",your_result = result_dic)

if __name__ == "__main__":
	app.run(threaded=False)