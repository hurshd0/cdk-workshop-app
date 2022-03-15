from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct
from cdk_dynamo_table_view import TableViewer

from .hitcounter import HitCounter


class CdkWorkshopAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. hello lambda function
        hello = _lambda.Function(
            self,
            "HelloHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda"),
            handler="hello.handler",
        )

        # 2. Hitcounter to count hits
        hitcounter = HitCounter(self, "HelloHitCounter", downstream=hello)

        # 3. API Endpoint to invoke the lambda function
        apigw.LambdaRestApi(self, "HitCountEndpoint", handler=hitcounter.handler)

        # 4. View the table
        TableViewer(self, "ViewHitCounter", table=hitcounter.table)
