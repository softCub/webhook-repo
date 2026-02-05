from flask import Flask
from webhook import webhook_route
from ui import ui_route

def create_app():
    app = Flask(__name__)
    app.register_blueprint(ui_route)
    app.register_blueprint(webhook_route)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
