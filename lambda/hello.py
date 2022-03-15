import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handler(event, context):
    try:
        logger.info(f"{json.dumps(event)}")
        result = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps(
                "Hello from CDK! You have hit {}.".format(event["path"])
            ),
        }
        logger.info(f"{json.dumps(result)}")
        return result
    except Exception as e:
        logger.error(e, exc_info=True)
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": e}),
        }
