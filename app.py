from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['post'])
def predict_placement():

    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')
    
    if (cgpa=="" or iq=="" or profile_score==""):
        result="Please Enter The values"
        return render_template('index.html',result=result )

    cgpa = float(cgpa)
    iq = int(iq)
    profile_score = int(profile_score)

    result = model.predict(np.array([cgpa, iq, profile_score]).reshape(1,3))
    print(result)

    if result[0]==0:
        result = 'Not Placed'
    else:
        result='Placed'

    return render_template('index.html', result=result)


if __name__=='__main__':
    #app.run(host="0.0.0.0", port=8080) this is for aws deployment
    app.run(debug=True)