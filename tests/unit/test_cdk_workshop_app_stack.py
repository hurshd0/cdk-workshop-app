from aws_cdk import Stack, aws_lambda as _lambda, assertions

from cdk_workshop_app.hitcounter import HitCounter
import pytest

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_workshopp_app/cdk_workshopp_app_stack.py
# from cdk_workshopp_app.cdk_workshopp_app_stack import CdkWorkshoppAppStack
# def test_sqs_queue_created():
#     app = core.App()
#     stack = CdkWorkshoppAppStack(app, "cdk-workshopp-app")
#     template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })


def test_dynamodb_table_created():
    stack = Stack()

    HitCounter(
        stack,
        "TestHitCounter",
        downstream=_lambda.Function(
            stack,
            "HelloHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="hello.handler",
            code=_lambda.Code.from_asset("lambda"),
        ),
    )

    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::DynamoDB::Table", 1)


def test_lambda_has_env_vars():
    stack = Stack()
    HitCounter(
        stack,
        "TestHitCounter",
        downstream=_lambda.Function(
            stack,
            "HelloHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="hello.handler",
            code=_lambda.Code.from_asset("lambda"),
        ),
    )
    template = assertions.Template.from_stack(stack)
    envCapture = assertions.Capture()

    template.has_resource_properties(
        "AWS::Lambda::Function",
        {"Handler": "hitcount.handler", "Environment": envCapture},
    )

    assert envCapture.as_object() == {
        "Variables": {
            "DOWNSTREAM_FUNCTION_NAME": {"Ref": "HelloHandler2E4FBA4D"},
            "HITS_TABLE_NAME": {"Ref": "TestHitCounterHits7D92E6DA"},
        }
    }


def test_dynamodb_with_encryption():
    stack = Stack()
    HitCounter(
        stack,
        "TestHitCounter",
        downstream=_lambda.Function(
            stack,
            "HelloHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="hello.handler",
            code=_lambda.Code.from_asset("lambda"),
        ),
    )
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties(
        "AWS::DynamoDB::Table",
        {
            "SSESpecification": {
                "SSEEnabled": True,
            }
        },
    )


def test_dynamodb_raises():
    stack = Stack()
    with pytest.raises(Exception):
        HitCounter(
            stack,
            "TestHitCounter",
            downstream=_lambda.Function(
                stack,
                "HelloHandler",
                runtime=_lambda.Runtime.PYTHON_3_9,
                handler="hello.handler",
                code=_lambda.Code.from_asset("lambda"),
            ),
            read_capacity=1,
        )
