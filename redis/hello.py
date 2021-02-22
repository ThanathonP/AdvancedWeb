import os
import redis
from flask import Flask,request,jsonify

#เชื่อมต่อกับ redis
app = Flask(__name__)
db=redis.StrictRedis(
        host='10.100.2.130',#เชื่อมต่อกับcloud
        port=6379,#port private ของ cloud
        password='RRRlax28813',#password 
        decode_responses=True)

#แสดงข้อมูลทั้งหมดใน Databass
@app.route('/',methods=['GET']) 
def Show_Animeall():
    name=db.keys()#ให้ตัวแปร name เก็บค่าตามKey ในDataBass
    name.sort()#ทำการเรียงข้อมูลname
    req = []#สร้างตัวแปร req
    for i in name :
        req.append(db.hgetall(i))#เพิ่มข้อมูลลงใน array ที่ชื่อ req ลงใน databass
    return jsonify(req)#ส่งค่าจากตัวแปร req

#แสดง1ข้อมูลทั้งหมดใน Databass
@app.route('/<Key>', methods=['GET'])
def Show_Anime(Key):
    name = db.hgetall(Key)#เพิ่มข้อมูลลงในตัวแปรที่ชื่อ req ลงใน databass
    return jsonify(name)#ส่งค่าจากตัวแปร req

#เพิ่มข้อมูลในDatabass
@app.route('/Key', methods=['POST'])
def add_Anime():
    id = request.json['ID']#insert ข้อมูล id
    name = request.json['name']#insert ข้อมูล id
    episode = request.json['episode']#insert ข้อมูล id
    user = {"ID":id, "name":name, "episode":episode}#ให้ตัวแปร user เก็บค่า id,name,episode
    db.hmset(name,user)#ส่งตัวแปร user ไปเพิ่ม databass
    return 'เพิ่มข้อมูลเรียบร้อย!!!'#return ข้อความว่า 'เพิ่มข้อมูลเรียบร้อย!!!'

#อัพเดทข้อมูลในตาราง
@app.route('/<Key>', methods=['PUT'])
def update_Anime(Key):
    id = request.json['ID']#แก้ไขข้อมูลให้กับตัวแปร id
    name = request.json['name']#แก้ไขข้อมูลให้กับตัวแปร name
    episode = request.json['episode']#แก้ไขข้อมูลให้กับตัวแปร episode
    user = {"ID":id, "name":name, "episode":episode}#ให้ตัวแปร user เก็บค่า id,name,episode
    db.hmset(name,user)#ส่งตัวแปร user ขึ้น databass โดยอ้างอิงจาก name
    return 'อัพเดทข้อมูลเรียบร้อย!!!'#return ข้อความว่า 'อัพเดทข้อมูลเรียบร้อย!!!'

#ลบข้อมูล
@app.route('/<Key>', methods=['DELETE'])
def delete_Anime(Key):
    db.delete(Key)#ลบข้อมูลใน databass โดยอ้างอิงจาก Key
    return 'ลบข้อมูลเรียบร้อย!!!'#return ข้อความว่า 'ลบข้อมูลเรียบร้อย!!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)