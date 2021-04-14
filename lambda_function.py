import pymongo
from pymongo import MongoClient
import urllib.parse
import datetime
from bson.json_util import dumps
import json
from bson.objectid import ObjectId
   
    
def lambda_handler(event, context):
    
    get_user_id = event['user_id']
    
    username = urllib.parse.quote_plus('myplanneradmin')
    password = urllib.parse.quote_plus('Myplanner@mongodb')

    url = "mongodb+srv://{}:{}@myplanner.9rjhm.mongodb.net/Myplanner?retryWrites=true&w=majority".format(username, password)
    client = MongoClient(url)
    mydb = client["Nomade"]


    user_Data = mydb['User']
            
    result = [i for i in user_Data.find({"_id": ObjectId(get_user_id)})]
    result = dumps(result)
    
    result = json.loads(result)
    if len(result) > 0:
        final_list=[]
        for x in result:
            all_data=x['info']
            val={'display_name' : x['display_name'],
                 'user_type' : x['user_type'],        
                 'email' : all_data.get('email'),
                 'password' : all_data.get('password')}
            final_list.append(val)
            
        print(final_list)
        return {
            'statusCode': 200,
            'body': ({'data':final_list})
        }
    else:
       return {
            'statusCode': 404,
            'body': ({'data':'Data Not Found'})
        }
   