from flask import Flask, request,render_template
from dotenv import load_dotenv
import pymongo
import os
load_dotenv()
client = pymongo.MongoClient(os.getenv("uri"))
db=client.test
collection=db['flask_db']
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
        form_data = dict(request.form)
        collection.insert_one(form_data)
        
        return 'form submitted successfully', 200
if __name__ == '__main__':
    app.run(debug=True)  # This starts the server on port 5000 by default
