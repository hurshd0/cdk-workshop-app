import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_workshopp_app.cdk_workshopp_app_stack import CdkWorkshoppAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_workshopp_app/cdk_workshopp_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkWorkshoppAppStack(app, "cdk-workshopp-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
