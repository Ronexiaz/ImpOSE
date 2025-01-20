from flask import Flask, request, jsonify
import server

dbOSE = server.dbBuilder()


def onCreate():
    currApp = Flask(__name__)

    with currApp.app_context():
        dbOSE.initDB()

    return currApp


app = onCreate()


@app.route("/")
def home():
    with dbOSE as (con, cursor):
        result, code = server.queryDB(con, cursor, server.queryBuilder())
        return result, code


@app.route("/get-by/<col>/<val>")
def getSpellByColumn(col, val):
    with dbOSE as (con, cursor):
        result, code = server.queryDB(con, cursor, server.queryBuilder(col, val))
        return result, code


@app.errorhandler(Exception)
def handleErrRequest(e):
    with dbOSE as (con, cursor):
        response, rCode = server.handleError(con, cursor, e)
        return response, rCode


@app.teardown_appcontext
def stopDB(exception):
    dbOSE.stop(exception)
