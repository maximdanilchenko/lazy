from flask import Flask, redirect

from .routes import site


app = Flask(__name__)

app.url_map.strict_slashes = False
app.register_blueprint(site)


@app.errorhandler(404)
def error_404(e):
    return redirect('')
