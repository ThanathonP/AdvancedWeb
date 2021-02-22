import os
import redis
from flask import Flask,request,jsonify

#connectRedis
app = Flask(__name__)
db=redis.StrictRedis(
        host='10.100.2.130',
        port=6379,
        password='RRRlax28813',
        decode_responses=True)

@app.route('/',methods=['GET']) 
def Show_Animeall():
    name=db.keys() 
    name.sort()
    req = []
    for i in name :
        req.append(db.hgetall(i))
    return jsonify(req)

# Get Single Staff
@app.route('/<Key>', methods=['GET'])
def Show_Anime(Key):
    name = db.hgetall(Key)
    return jsonify(name)

#ใส่ข้อมูลเพิ่มในตาราง
@app.route('/Key', methods=['POST'])
def add_Anime():
    id = request.json['ID']
    name = request.json['name']
    episode = request.json['episode']
    user = {"ID":id, "name":name, "episode":episode}
    db.hmset(name,user)
    return 'เเก้ด้วย'

#อัพเดทข้อมูลในตาราง
@app.route('/<Key>', methods=['PUT'])
def update_fruit(Key):
    id = request.json['ID']
    name = request.json['name']
    episode = request.json['episode']
    user = {"ID":id, "name":name, "episode":episode}
    db.hmset(name,user)
    return 'Update data success!!!'

#ลบข้อมูล
@app.route('/<Key>', methods=['DELETE'])
def delete_staff(Key):
    db.delete(Key)
    return 'Delete data success!!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)