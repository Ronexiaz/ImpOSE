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
        return server.getAllSpells(con, cursor), 200


@app.route("/get-by-id/<spellID>")
def getSpellByID(spellID):
    with dbOSE as (con, cursor):
        try:
            response = server.getSpellByID(con, cursor, spellID)
            return response, 200
        except TypeError as e:
            return e


@app.route("/get-by-name/<name>")
def getSpellByName(name):
    with dbOSE as (con, cursor):
        response = server.getSpellByName(con, cursor, name)
        return response, 200


@app.route("/get-by-level/<level>")
def getSpellByLevel(level):
    with dbOSE as (con, cursor):
        response = server.getSpellByLevel(con, cursor, level)
        return response, 200


@app.teardown_appcontext
def stop_db(exception):
    dbOSE.stop(exception)
