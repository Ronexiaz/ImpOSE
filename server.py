import werkzeug
import database
import datetime as dt
import logging


def handleError(connection, cursor, exception):
    eStatement = ("Error found at time: " + str(dt.datetime.now()) + "\nWith cursor at: " + str(cursor.lastrowid)
                  + "\nDescription: " + exception.description)
    logging.error("\n" + eStatement + "\nResponse: " + str(exception.response))
    return eStatement, exception.response


def dbBuilder():
    return database.OSEDatabase()


def parseString(string):
    pString = string.replace("_", " ")
    return pString


def queryBuilder(column=None, val=""):
    query = r'SELECT * FROM SPELL_TABLE'
    if column is None:
        return query
    query += r' WHERE ' + column + ' IS '
    match column:
        case 'Name' | 'Duration' | 'Range':
            query += r'"' + parseString(val) + r'"'
        case 'Class':
            query += r'"' + val.upper() + r'"'
        case 'Spell_ID' | 'Level':
            query += val
        case _:
            raise werkzeug.exceptions.BadRequest
    return query


def queryDB(connection, cursor, query, args=(), one=False):
    spells = []
    result = cursor.execute(query).fetchall()
    if len(result) == 0:
        raise werkzeug.exceptions.BadRequest("Failure to find any matching rows. "
                                             "Check the spelling and try again.", 400)
    for spell in result:
        currSpell = dict((cursor.description[idx][0], value)
                         for idx, value in enumerate(spell))
        spells.append(currSpell)
    return spells, 200
