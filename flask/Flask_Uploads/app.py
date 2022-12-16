import os
from flask import Flask, flash, render_template, request
# please note the import from `flask_uploads` - not `flask_reuploaded`!!
# this is done on purpose to stay compatible with `Flask-Uploads`
from flask_uploads import IMAGES, UploadSet, configure_uploads

from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__, static_url_path='/static')

app.config["SECRET_KEY"] = os.urandom(24)
app.config["UPLOADED_PHOTOS_DEST"] = "static/img"
app.config["UPLOADED_PHOTOS_URL"] = "static/img"

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

from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class FormUploads(FlaskForm):
    btn_uploads = FileField('uploads', validators=[
        FileAllowed(photos, 'IMAGE ONLY'),
        FileRequired('IMAGE REQUIRED PLEASE')
    ])
    submit = SubmitField('Upload_IMG')

@app.route('/upload_wtf/', methods=['GET','POST'])
def upload_wtf():
    form = FormUploads()
    if form.validate_on_submit():
        file_name = photos.save(form.btn_uploads.data)
        file_url = photos.url(file_name)
        print(file_name, file_url)
        return render_template('abc.html', form=form, file_name=file_name, file_url=file_url)
    else:
        file_name = None
        file_url = None
    return render_template('abc.html', form=form, file_name=file_name, file_url=file_url)

if __name__ == '__main__':
    app.run(debug=True)