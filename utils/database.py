from .databaseConnection import DatabaseConnection


def create_password_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS passwords(application text primary key, password text)')


def add_password(app, password):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO passwords VALUES(?,?)', (app, password))


def list_passwords():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * from passwords')

        #cursor.fetchall() gives the list of tuples [(application1,password1), (application2,password2)]

        passwords = [{'application' : row[0], 'password' : row[1]} for row in cursor.fetchall()]

        return passwords


def delete_password(app):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM passwords WHERE application=?', (app,))