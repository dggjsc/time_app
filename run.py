from flask import Flask
app = Flask(__name__)


@app.route('/time')
def time():
    from time import gmtime, strftime
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
