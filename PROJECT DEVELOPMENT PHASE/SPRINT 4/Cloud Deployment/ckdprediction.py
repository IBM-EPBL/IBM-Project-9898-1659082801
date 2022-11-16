from flask import Flask,render_template,request
import numpy as np
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "a-qUIpHZUwdZyhqTXKdDX9PKskdMto90F2YK-FEe1VTw"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

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
        data = [[int(age),float(bp),float(sg),float(al),float(su),float(rbc),float(pc),float(pcc),float(ba),float(bgr),float(bu),float(sc),float(sod),float(pot),float(hemo),float(wc),float(rc),float(htn),float(dm),float(cad),float(appet),float(pe),float(ane)]]
        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": [age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,wc,rc,htn,dm,cad,appet,pe,ane], "values": data}]}

        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3aadc0e4-27aa-434f-9875-9abaed603306/predictions?version=2022-11-15', json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
        print("Scoring response")
        pred=response_scoring.json()
        output=pred['predictions'][0]['values'][0][0]
        print(output)
        return render_template("result.html",prediction=output)

if __name__ == '__main__':
	app.run(debug=True)
