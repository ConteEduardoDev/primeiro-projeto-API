from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'FIUJ@!AFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
with app.app_context():
    db = SQLAlchemy(app)
    db: SQLAlchemy

    class Postagem(db.Model):
        __tablename__ = 'postagem'
        id_postagem = db.Column(db.Integer, primary_key=True)
        titulo = db.Column(db.String)
        id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

    class Autor(db.Model):
        __tablename__ = 'autor'
        id_autor = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String)
        email = db.Column(db.String)
        senha = db.Column(db.String)
        admin = db.Column(db.Boolean)
        postagens = db.relationship('Postagem')
        
    def inicializar_banco():
        db.drop_all()
        db.create_all()

        autor = Autor(nome='Eduardo', email='eduardo@email.com',
                    senha='123456789', admin=True)
        db.session.add(autor)
        db.session.commit()

    if __name__ == "__main__":
        inicializar_banco()