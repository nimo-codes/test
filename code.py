

from flask import Flask, jsonify, request, render_template
import pickle
import numpy as np


# creating a Flask app
app = Flask(__name__,template_folder='template')




def load_model_give_res():
    filename = "/Users/jarvis/pymycod/tensorflow_AI/trained_models/lr_model_wine_quality.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    u1 = float(request.form.get('FA'))
    u2 = float(request.form.get('VA'))
    u3 = float(request.form.get('CA'))
    u4 = float(request.form.get('PH'))
    u5 = float(request.form.get('SH'))
    u6 = float(request.form.get('AL'))
    print(u1)
    l1 = np.array([u1,u2,u3,u4,u5,u6])
    result = loaded_model.predict([l1])
    print(result)




# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    # if(request.method == 'GET'):
  
    #     data = "hello world"
    #     return jsonify({'data': data})
    if request.method == "POST":
        print("Fvfrfvefvcdfcvghfdsvgtytrefc")
        load_model_give_res()
    return render_template("form.html")   

        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
