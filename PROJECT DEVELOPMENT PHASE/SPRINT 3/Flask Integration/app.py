# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np



# Load the Random Forest CLassifier model
filename = 'RandomForest.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')

def formpg():
    return render_template('main.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        age =request.form.get('age')
        bp = request.form.get('bp')
        sg = request.form.get('sg')
        al = request.form.get('al')
        su = request.form.get('su')
        rbc = request.form.get('rbc')
        pc = request.form.get('pc')
        pcc = request.form.get('pcc')
        ba = request.form.get('ba')
        bgr = request.form.get('bgr')
        bu = request.form.get('bu')
        sc = request.form.get('sc')
        sod = request.form.get('sod')
        pot = request.form.get('pot')
        hemo = request.form.get('hemo')
        wc = request.form.get('wc')
        rc = request.form.get('rc')
        htn = request.form.get('htn')
        dm = request.form.get('dm')
        cad = request.form.get('cad')
        appet = request.form.get('appet')
        pe = request.form.get('pe')
        ane = request.form.get('ane')
        
        data = np.array([[age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,wc,rc,htn,dm,cad,appet,pe,ane]])
        my_prediction = model.predict(data)
        

        return render_template('result.html', prediction=my_prediction)
        
        

if __name__ == '__main__':
	app.run(debug=True)
