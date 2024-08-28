from flask import Flask
from flask_graphql import GraphQLView
from .schema import schema

def create_app():
    app = Flask(__name__)

    # 配置 GraphQL 路由
    app.add_url_rule(
        '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )

    return app