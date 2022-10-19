from flask import Flask
from flask import request
from flask import Response
import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.toy.bolt import BOLT
from spherov2.types import Color
import threading

#Ryan's part
import pymysql
import random
# conn = pymysql.connect(host='raas-data.c9q9qv3ngmbu.us-east-2.rds.amazonaws.com',user='admin',password='gK?7Rrg-5hHtS?s12',database='raas-data')
# cursor = conn.cursor()

# def com(x,n,bid):
#    randomList2 = [-1,0,1]
#    insert_query = '''
#                INSERT INTO dataTest VALUES
#                (%s,%s,%s,%s);
#               
#                '''
#    values = (x[0],x[1],n,bid)
#    cursor.execute(insert_query,values)
#    conn.commit()
#Ryan's part end
app = Flask(__name__)


@app.route("/execute", methods=['POST'])
def execute():
    global batch_id
    input = request.json
    print(str(request.json))
    print(input['commands'])
    toys = scanner.find_toys(toy_names=['SB-F6D6'], toy_types=[BOLT])
    print(str(len(toys)) + '/' + str(len(['SB-F6D6'])) +' robots found')
    print("Getting batch number...")
    fetch_query = 'select id from seq;'
    # cursor.execute(fetch_query)
    # bid = cursor.fetchone()
    # print(bid[0])
    # batch_id = bid[0] + 1
    # batch_query = 'update seq set id = ' + str(batch_id)
    # cursor.execute(batch_query)
    # conn.commit()
    # print("Batch number "+ str(batch_id)+"!")
    for toy in toys:
        thread = threading.Thread(target=run_the_robot, args=(toy, input['commands']))
        thread.start()
        #run_the_robot(toy, input['commands'])
        time.sleep(1)
    return Response('Success')

@app.route("/runPolicy", methods=['POST'])
def run_policy():
    input = request.json
    toy = scanner.find_toy(toy_name='SB-F6D6', toy_types=[BOLT])
    #policy = [[1,1,1,1,3],[3,1,1,1,4],[4,1,1,1,3],[3,1,1,1,4],[4,1,1,1,0]]
    policy = [[0,0,90],[90,180,180],[0,0,0]]
    try:
        with SpheroEduAPI(toy) as droid:
            print(toy.name + ' started!')
            droid.set_main_led(Color(r=0, g=0, b=255))
            droid.roll(0, 80, 1.1)
            time.sleep(2)
            while droid.get_location()['x'] < 95 or droid.get_location()['y'] < 95:
                x = droid.get_location()['x']
                y = droid.get_location()['y']
                print(str(x) + ' ' + str(y))
                step = policy[int(x/46)][int(y/46)]
                if step == 0:
                    droid.roll(0, 80, 1.1)
                    time.sleep(2)
                elif step == 90:
                    droid.roll(90, 80, 1.1)
                    time.sleep(2)
                    
                elif step == 180:
                    droid.roll(180, 80, 1.1)
                    time.sleep(2)
                elif step == 270:
                    droid.roll(270, 80, 1.1)
                    time.sleep(2)
                else:
                    droid.stop_roll()
                    break
            print(str(droid.get_location()['x']) + ' ' + str(droid.get_location()['y']))
            droid.stop_roll()
    except Exception as e:
        print('Connection failed with ' + toy.name)
        print("error :" +str(e))
    return Response('Success')
    
def run_the_robot(toy, commands):
    try:
        with SpheroEduAPI(toy) as droid:
            print(toy.name + ' started!')
            loc = [0.00,0.00]
            action = "up"
            droid.set_main_led(Color(r=0, g=0, b=255))
            for c in commands.split(','):
                if c.startswith('roll'):
                    params = c.split(';')
                    droid.roll(int(params[1]), int(params[2]), float(params[3]))
                    #Ryan's part
                    if(int(params[1]) == 0 or int(params[1]) == 360):
                        action = "up"
                    elif(int(params[1]) == 90):
                        action = "right"
                    elif(int(params[1]) == 180):
                        action = "down"
                    elif(int(params[1]) == 270):
                        action = "left"
                    #Ryan's part end
                    print(toy.name + ' rolling at ' + params[1] + ' degree ' + 'with speed ' + params[2] + ' for ' + params[3] + 'secs')
                elif c.startswith('set_speed'):
                    params = c.split(';')
                    droid.set_speed(int(params[1]))
                    print(toy.name + ' setting speed to ' + params[1])
                elif c.startswith('stop_roll'):
                    droid.stop_roll()
                    print(toy.name + ' stopped rolling')
                elif c.startswith('set_heading'):
                    params = c.split(';')
                    droid.set_heading(int(params[1]))
                    print(toy.name + ' heading at ' + params[1] + ' degree angle')
                elif c.startswith('spin'):
                    params = c.split(';')
                    droid.spin(int(params[1]), int(params[2]))
                    print(toy.name + ' spinning at ' + params[1] + ' degree ' + 'for ' + params[2] + ' secs')
                elif c.startswith('reset_aim'):
                    droid.reset_aim()
                    print(toy.name + ' resetting aim to 0 degree')
                elif c.startswith('sleep'):
                    params = c.split(';')
                    print(toy.name + ' continuing for ' + params[1] + ' secs')
                    time.sleep(int(params[1]))
                #Ryan's part
                pre_loc = list(droid.get_location().values())
                loc = [ '%.2f' % elem for elem in pre_loc ]
                # com(loc,toy.name,batch_id)
                #Ryan's part end
            print(toy.name + ' stopped!')
    except Exception as e:
        print('Connection failed with ' + toy.name)
        print("error :" +str(e))
        print('Reconnecting to ' + toy.name)
        toy = scanner.find_toy(toy_name=toy.name, toy_types=[BOLT])
        run_the_robot(toy, commands)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


