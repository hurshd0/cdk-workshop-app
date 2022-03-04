import json
import logging
import sys

logger = logging.getLogger()
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


def handler(event, context):
    try:
        logger.info("[INPUT] REQUEST: event: {}".format(event))
        result = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps("Hello, CDK! You have hit {}\n".format(event["path"])),
        }
        logger.info("[OUTPUT] RESPONSE: result: {}".format(result))
        return result
    except Exception as e:
        logger.error("[ERROR] {}".format(e), exec_info=True)
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": repr(e)}),
        }


def main():
    dummy_event = {"path": "/hello"}
    context = {}
    handler(dummy_event, context)


if __name__ == "__main__":
    main()
