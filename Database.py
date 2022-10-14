import boto3
import time
import datetime
from boto3.dynamodb.conditions import Key, Attr


class DynamoDb:
    def __init__(self,dbname,table_name):
        self._dbname = dbname
        self._table_name = table_name
        self.dynamo_db_conn = boto3.resource(self._dbname)
        self.table_intialization = self.dynamo_db_conn.Table(self._table_name)
    
    def fetch_single_minute_data(self,timestamp,datatype):
        response = self.table_intialization.scan(FilterExpression=Attr('datatype').begins_with(datatype.capitalize()) & Attr('timestamp').eq(timestamp))
        if response == []:
            print(f'Data not available for {datatype}')
        return response['Items']
    
    def fetch_total_data(self,deviceid):
        response = self.table_intialization.query(KeyConditionExpression=Key('deviceid').eq(deviceid))
        return response

    