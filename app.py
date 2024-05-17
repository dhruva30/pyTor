from flask import Flask, request
import os

import functions

app = Flask(__name__)


@app.route("/torrents", methods=["GET"])
def search_torrents():
    query = request.args.get("query")
    page = request.args.get("page")
    return functions.search_torrents(query, page)


@app.route("/", methods=["GET"])
def health():
    return "OK"
