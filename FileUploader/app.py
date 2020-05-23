import os
import aws.recognizer as reco
from flask import Flask, render_template, request

app = Flask(__name__, static_folder="images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Could'n create upload directory: {}".format(target))

    print(request.files.getlist("file"))

    for upload in request.files.getlist("file"):
        filename = upload.filename
        destination = "/".join([target, filename])
        upload.save(destination)
        print('=====================================================================================================')
        list_names = reco.get_labels(filename)
    return render_template("complete.html", image_name=filename, founded_list=list_names)


if __name__ == "__main__":
    app.run(port=4555, debug=True)
