from website import create_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = create_app()

# attempted at making a database. could not get it to work
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
# db = SQLAlchemy(app)

# app.app_context().push()

# class accounts(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
#     def __repr__(self):
#         return '<Name %r>' % self.id


if __name__ == '__main__':
    app.run(debug=True)

