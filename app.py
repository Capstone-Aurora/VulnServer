from flask import Flask, send_file
from flask_restx import Api, Resource, reqparse, fields
import requests
import json
import shell_command
import threading
import time

app = Flask(__name__)

api = Api(app, version='1.0', title='OSVCAT 문서', description='OSVCAT API 문서', doc="/api-docs")

SearchVuln = api.namespace('SearchVuln', description='취약점 조회 API')
SearchDep = api.namespace('SearchDep', description='의존성 조회 API')

def searchvuln(name, version) :
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
    return response.json()

def searchdep(file_content) :
    with open("requirments.txt", 'w') as file:
        file.write(file_content)
    t1 = threading.Thread(target=shell_command.command)
    t1.daemon = True 
    t1.start()
    while(not shell_command.check_string_in_file()) :
        time.sleep(3)
    return "http://pwnable.co.kr/dependencies.png"

ModelVuln = SearchVuln.model('SearchVuln', strict=True, model={
    'name': fields.String(title='패키지명', default='mruby', required=True),
    'version': fields.String(title='버전정보', default='2.1.2rc', required=True),
})

ModelDep = SearchDep.model('SearchDep', strict=True, model={
    'file': fields.String(title='파일정보', default='brotlipy==0.7.0\ncertifi==2022.12.7\ncffi==1.15.1', required=True),
})

@SearchDep.route('/')
class Test(Resource):
    @SearchDep.expect(ModelDep)
    def post(self):
        return (searchdep(api.payload['file'])), 200

@SearchVuln.route('/')
class Test(Resource):
    @SearchVuln.expect(ModelVuln)
    def post(self):
        return (searchvuln(api.payload['name'], api.payload['version'])), 200


if __name__ == '__main__':
    app.run(debug=True)