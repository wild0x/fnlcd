from flask import Flask,jsonify,request
from prediction import predict_result

app = Flask(__name__)

stores=[1]

@app.route('/',methods=['POST'])
def create_store():
    request_data=request.form
    new_store={'name':request_data['name']}
    stores[0]=(new_store)
    return jsonify(new_store)
	
	

@app.route('/')
def get_store():	
	return jsonify({'result':str(predict_result(stores))}) 
	
@app.errorhandler(500)
def internal_error(error):
	return  jsonify({'result':'2'})


	
if __name__ == "__main__":
    app.run(port=5000)