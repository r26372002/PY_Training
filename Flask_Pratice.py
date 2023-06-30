import flask as Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world"


@app.route('/test')
def test():
    return "This is a test!"


if __name__ == "__main__":
    app.run()
