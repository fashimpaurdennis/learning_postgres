from flask_app import app

@app.route('/')
def render_home():
    return {
        'message': 'stuff goes here'
    }
