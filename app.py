import flask
from flask import Flask


app = Flask(__name__)

global_storage =[]

@app.route('/storestring' , methods=['POST'])
def store_strings():
  print("hello")
  json_data = flask.request.json
  a_value = json_data["hello"]
  global_storage.append(a_value)
  print("GLOBAL :", global_storage)
  return "JSON value sent: " + a_value

@app.route("/concatStrings")
def get_concat_strings():
  print("GLOBAL :", global_storage)
  str=""
  for s in global_storage:
    str = str +s
  return str



def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run(debug=True)