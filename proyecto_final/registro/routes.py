from registro import app

@app.route("/")
def index():
    return "Esto es Flask JS"