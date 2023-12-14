import json
from flask import Flask, request
from jose import jwt

from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)



@app.route('/')
def hello_world():
    #print(request.headers)
    token = request.headers['Authorization'].split(" ")
    jsonReturn= {}
    print(token[1])
    decoded = jwt.decode(token[1],key=None,options={"verify_signature":False,"verify_aud": False,},algorithms='RS256')
    jsonReturn['jwt']= decoded
    for header in request.headers:
        print(header)
        jsonReturn[header[0]]= header[1]
        

    return jsonReturn

#
# This is the check to keep the pod alive
# if this fails k8s will restart the pod
@metrics.do_not_track()
@app.route('/health')
def health():
    return 'Everything is Good!'

#
# This is the check that lets the pod accepts trafffic
# if this fails k8s will not send any more traffic to this pod
@metrics.do_not_track()
@app.route('/ready')
def ready():
    return 'Im ready to work!'


#
# /metrics endpint is alive and send prometheus metrics
#  
#
#