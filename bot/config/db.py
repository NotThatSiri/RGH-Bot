from pony import orm
from config import loadconfig


db = Database()

class User(db.Entity):
    id = PrimaryKey(int, auto=False)
    name = Required(str)
    mention = Required(str)

class Type(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    
class Guild(db.Entity):
    id = PrimaryKey(int, auto=False)
    name = Required(str)
    owner = Set('User')

class Action(db.Entity):
    id = PrimaryKey(int, auto=True)
    server = Set('Guild')
    moderator = Set('User')
    type = Set('Type')
    offender = Set('User')
    reason = Optional(str)
    timestamp = Required(datetime)

db_host = loadconfig.__db__['host']
db_user = loadconfig.__db__['user']
db_passwd = loadconfig.__db__['passwd']
db_db = loadconfig.__db__['db']
db.bind(provider='mysql', db_host, db_user, db_passwd, db_db)
db.generate_mapping(create_tables=True)
