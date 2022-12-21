import json
import plotly as py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 設置圓餅圖資料
    pie = {
        'values': [100, 50, 30, 20],
        'labels': ['香蕉', '蘋果', '水梨', '草莓'],
        'type': 'pie'
    }
    xy = {
        'values': [100, 50, 90, 50],
        'labels': ['香蕉', '蘋果', '水梨', '草莓'],
        'type': 'pie'
    }

    graphs = [
        dict(
            data=[
                pie
            ],
            layout=dict(
                width='100%',
                height='100%'
            )
        )
    ]

    # 序列化
    graphJSON = json.dumps(graphs, cls=py.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.debug = True
    app.run()