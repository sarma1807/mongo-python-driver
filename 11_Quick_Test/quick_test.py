import pymongo

mongo_conn_str = "mongodb://192.168.1.151:1807/"
client = pymongo.MongoClient(mongo_conn_str)

try:
    print("Connected to MongoDB Server Version : " + client.server_info()['version'])
    print("Connection String : " + mongo_conn_str)

except Exception:
    print("Unable to connect to the server.")


