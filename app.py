from flask import Flask, make_response, request, render_template
import io
import csv

app = Flask(__name__)

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")


@app.route('/')

def index():
    return render_template('home.html')

def form():
    return """
        <html>
            <body>
                <h1>Transform a file demo</h1>

                <form action="/submit" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

@app.route('/submit', methods=["POST"])
def transform_view():
    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("iso8859_15"), newline=None)
    csv_input = csv.reader(stream)
    #print("file contents: ", file_contents)
    #print(type(file_contents))
    print(csv_input)
    for row in csv_input:
        print(row)

    stream.seek(0)
    result = transform(stream.read())

    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    return response

if __name__ == "__main__":
    app.run(debug=True)