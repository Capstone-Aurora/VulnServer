from flask import Flask
from flask_restx import Api, Resource, reqparse, fields
import requests
import json

app = Flask(__name__)

api = Api(app, version='1.0', title='OSVCAT 문서', description='OSVCAT API 문서', doc="/api-docs")

test_api = api.namespace('SearchVuln', description='조회 API')

@app.route('/SearchVuln', methods = ['POST'])
def SearchVuln():
    user = request.get_json()#json 데이터를 받아옴
    print(user)
    return jsonify(user)# 받아온 데이터를 다시 전송


'''    
#def search(name, version) :
    url = "https://api.osv.dev/v1/query"
    data = {
        "package": {
            "name": name
        },
        "version": version
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    print(response.json())
'''
model = test_api.model('new article', strict=True, model={
    'name': fields.String(title='패키지명', default='mruby', required=True),
    'version': fields.String(title='버전정보', default='2.1.2rc', required=True),
})

@test_api.route('/')
class Test(Resource):
    @staticmethod
    @test_api.expect(model, validate=True)
    def post():
    	return search(model.name, model.version)




if __name__ == '__main__':
    app.run(debug=True)