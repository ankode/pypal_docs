

from boto3.dynamodb.conditions import Key, Attr
import boto3

dynamodb = boto3.resource('dynamodb',region_name='us-west-2')
table = dynamodb.Table('test')
def insert(mobile,param):
    response=table.put_item(
    Item=param)
    return response


param={'key': 'pypal',
            'column_1': 'amazon '}
# print(insert('key',param))


def query(key):
    response = table.query(
        KeyConditionExpression=Key('key').eq(key),
        Limit=15
            )
    return response

# print (query('key1'))

def update(key,param):
    response=table.update_item(
        Key= {'key': key },
        AttributeUpdates=param,
        ReturnValues='ALL_NEW'
    )
    return response

param={"city": {"Value": 'manipal'}}
print(update('key1',param))
