import os
from flask import Flask, flash, render_template, request
# please note the import from `flask_uploads` - not `flask_reuploaded`!!
# this is done on purpose to stay compatible with `Flask-Uploads`
from flask_uploads import IMAGES, UploadSet, configure_uploads

from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(24)
app.config["UPLOADED_PHOTOS_DEST"] = "static/img"

photos = UploadSet("photos", IMAGES)
configure_uploads(app, photos)

@app.route("/", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:

        # 檔名處理
        file_name_hz = secure_filename(request.files['photo'].filename).split('.')[-1]
        first_name = str(uuid.uuid4())
        file_name = first_name + '.' + file_name_hz

        photos.save(request.files['photo'],name=file_name)

        flash("Photo saved successfully.")
        return render_template('upload.html')
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)