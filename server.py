import database


def dbBuilder():
    return database.OSEDatabase()


def queryDB(connection, cursor, query, args=(), one=False):
    result = cursor.execute(query, args).fetchall()
    return result


def parseName(name):
    pName = name.replace("_", " ")
    return pName


def getAllSpells(connection, cursor):
    spells = []
    query = queryDB(connection, cursor, '''SELECT * FROM SPELL_TABLE''')
    for spell in query:
        currSpell = dict((cursor.description[idx][0], value)
                         for idx, value in enumerate(spell))
        spells.append(currSpell)
    return spells


def getSpellByID(connection, cursor, spellID):
    statement = '''SELECT * FROM SPELL_TABLE WHERE Spell_ID IS ''' + spellID
    query = dict((cursor.description[idx][0], value)
                 for idx, value in
                 enumerate(cursor.execute(statement).fetchone()))
    return query


def getSpellByName(connection, cursor, name):
    spells = []
    query = queryDB(connection, cursor, '''SELECT * FROM SPELL_TABLE WHERE Name IS \"''' + parseName(name) + '''\"''')
    for spell in query:
        currSpell = dict((cursor.description[idx][0], value)
                         for idx, value in enumerate(spell))
        spells.append(currSpell)
    return spells


def getSpellByLevel(connection, cursor, level):
    spells = []
    query = queryDB(connection, cursor, '''SELECT * FROM SPELL_TABLE WHERE Level = ''' + level)
    for spell in query:
        currSpell = dict((cursor.description[idx][0], value)
                         for idx, value in enumerate(spell))
        spells.append(currSpell)
    return query
