from constructs import Construct
from aws_cdk import Stack
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep


class WorkshopPipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        pipeline = CodePipeline(self, "Pipeline", 
                                pipeline_name = "CDKWorkshopPipeline",
                                synth=ShellStep(
                                    "Synth",
                                                )