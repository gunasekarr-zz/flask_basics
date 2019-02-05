from flask import Flask
from models import db

app = Flask(__name__)

# #Postgres connection
# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'guna3453amu',
#     'db': 'catalog_db',
#     'host': 'localhost',
#     'port': '5432',
# }

# #app configuration settings and #\ is a new break line indicator in second line
# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
# app.config[SQLALCHEMY_TRACK_MODIFICATION] = False

# #app configuration settings and #\ is a new break line indicator in second line
# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
# app.config[SQLALCHEMY_TRACK_MODIFICATION] = False


#Postgre DB connection string

#SQLALCHEMY_DATABASE_URI='<dbname>://<userid>:<pswd>@<host:port>/<db_name>',

app.config.update(
    DEBUG = True,
    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:guna3453amu@localhost:5432/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(app)

#for single quote pls enclose the same with double quote but ensure you separate the senetnces with single quote
@app.route("/")
def main():
    return 'Welcome to Guna' "'"'s homepage!'

if __name__ == '__main__':
    app.run()