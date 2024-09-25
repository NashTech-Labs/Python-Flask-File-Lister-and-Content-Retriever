from flask import Flask, send_file, request
import os

app = Flask(__name__)

a = []

@app.route('/')
def list_files_recursive(path='/home/ubuntu/'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            a.append({"filetype":"dir","path":full_path})
            list_files_recursive(full_path)
        else:
            a.append({"filetype":"file","path":full_path})
    return a

@app.route('/getfilecontent')
def returnContentofFile():
    data = request.get_json()
    filepath = data["path"]
    if(os.path.exists(filepath)):
        if os.path.isdir(filepath):
            return {"error":"filetype is directory"},404
        else:
            return send_file(filepath)
    else:
        return {"error":"Invalid file Path"},404
        
    
app.run('0.0.0.0',4000,debug=True)