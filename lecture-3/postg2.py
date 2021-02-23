from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import column

#Init app
app = Flask(__name__)

#Database
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://webadmin:HBVgsc17776@node8589-advweb-15.app.ruk-com.cloud:11097/Animes"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://webadmin:HBVgsc17776@10.100.2.185:5432/Animes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
#Init db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)

#Staff Class/Model
class animed(db.Model):
    id = db.Column(db.String(8), primary_key=True, unique=True)
    name = db.Column(db.String(50))
    episode = db.Column(db.String(10))
    
    def __init__(self, id, name, episode):
        self.id = id
        self.name = name
        self.episode = episode

# Staff Schema
class AnimeSchema(ma.Schema):
    class Meta:
        fields =('id', 'name', 'episode')

# Init Schema 
staff_schema = AnimeSchema()
staffs_schema = AnimeSchema(many=True)

# Get All Staffs
@app.route('/staffs', methods=['GET'])
def get_staffs():
    all_staffs = animed.query.all()
    result = staffs_schema.dump(all_staffs)
    return jsonify(result)

# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello Cloud DB1'})

# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)