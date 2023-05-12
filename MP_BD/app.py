from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajouter', methods=['POST'])
def ajouter():
    codPiece = request.form['codPiece']
    qtestck = request.form['qtestck']
    type = request.form['type']

    # Connectez-vous à la base de données
    cnx = mysql.connector.connect(user='root', password='admin',
                                  host='localhost',
                                  database='mp_bd2')
    cursor = cnx.cursor()

    # Insérez une nouvelle entrée dans la table
    query = "INSERT INTO Piece (codPiece, qtestck, type) VALUES (%s, %s, %s)"
    data = (codPiece, qtestck, type)
    cursor.execute(query, data)
    cnx.commit()
    

    # Fermez la connexion à la base de données
    cursor.close()
    cnx.close()

    # Retournez une réponse HTTP
    message = 'Pièce ajoutée avec succès!'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
