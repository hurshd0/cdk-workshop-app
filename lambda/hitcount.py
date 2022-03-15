import json
import os
import logging
import boto3


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


ddb = boto3.resource("dynamodb")
table = ddb.Table(os.environ["HITS_TABLE_NAME"])
_lambda = boto3.client("lambda")


def handler(event, context):
    try:
        logger.info(f"{json.dumps(event)}")
        table.update_item(
            Key={"path": event["path"]},
            UpdateExpression="ADD hits :incr",
            ExpressionAttributeValues={":incr": 1},
        )
        resp = _lambda.invoke(
            FunctionName=os.environ["DOWNSTREAM_FUNCTION_NAME"],
            Payload=json.dumps(event),
        )
        body = resp["Payload"].read().decode("utf-8")
        logger.info(f"{body}")
        return json.loads(body)

    except Exception as e:
        logger.error(e, exc_info=True)
