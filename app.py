from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare"]
collection = db["patients"]

@app.route('/', methods=['GET', 'POST'])
def home():
    success = False

    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        phone = request.form.get('phone')
        email = request.form.get('email')
        msg = request.form.get('msg')

        data = {
            "name": name,
            "age": age,
            "gender": gender,
            "phone": phone,
            "email": email,
            "message": msg
        }

        collection.insert_one(data)
        success = True

    return render_template("index.html", success=success)


if __name__ == '__main__':
    app.run(debug=True, port=5003)