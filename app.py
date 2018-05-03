from flask import Flask, make_response, request, render_template
import io
import csv
import collections

# https://github.com/twbs/bootstrap/issues/20813

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/results', methods=["POST"])

def results():
    stores = []
    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("iso8859_15"), newline='')
    csv_input = csv.reader(stream)

    for row in csv_input:
        #del row[0]
        if 'D' in row[8]: #Check for debit not credit
            stores.append(row[3])

    del stores[0]
    stores = set(stores)

    return render_template('results.html',stores=stores)

@app.route('/', methods=["POST"])

def storeReturn():
    if request.method == 'POST':
        storeValue = request.form.get("storeValue")
        print(storeValue)

if __name__ == "__main__":
    app.run(debug=True)