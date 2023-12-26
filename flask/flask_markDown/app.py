from flaskext.markdown import Markdown

from flask import Flask, render_template, url_for,redirect
from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from flask_pagedown import PageDown
from wtforms.fields import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY']='your key'

Markdown(app)
PageDown(app)


@app.route('/')
def index():
    return render_template('test.html')

mk = """
# h1
## h2
### h3
#### h4
"""

@app.route('/test1')
def index1():
    return render_template('test1.html', post=mk)

# ---------------------------------*

class PageDownFormExample(FlaskForm):
    #  加入一個form，單純的一個PageDownField跟提交欄位測試
    pagedown = PageDownField('Enter your markdown')
    submit = SubmitField('Submit')

@app.route('/test2', methods = ['GET', 'POST'])
def index2():
    form = PageDownFormExample()
    if form.validate_on_submit():
        text = form.pagedown.data
        return text
    return render_template('markdown_test.html', form = form)




if __name__ == '__main__':
    app.debug=True
    app.run()