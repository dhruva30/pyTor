from flask import Flask, request

import functions

app = Flask(__name__)


@app.route("/torrents", methods=["GET"])
def search_torrents():
    query = request.args.get("query")
    page = request.args.get("page")
    return functions.search_torrents(query, page)

app.run(host='0.0.0.0', port=5000)