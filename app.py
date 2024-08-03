# app.py
from flask import Flask, render_template
import uuid

app = Flask(__name__, template_folder='templates')

@app.route('/')
def generate_uuid():
    my_uuid = str(uuid.uuid4())
    return render_template('index.html', uuid=my_uuid)

if __name__ == '__main__':
    app.run(debug=True)
