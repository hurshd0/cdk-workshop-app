from constructs import Construct
from aws_cdk import Stage
from .cdk_workshop_app_stack import CdkWorkshopAppStack


class WorkshopPipelineStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = CdkWorkshopAppStack(self, "WebService")
