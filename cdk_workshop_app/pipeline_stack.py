from constructs import Construct
from aws_cdk import Stack
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
import aws_cdk as cdk
from .pipeline_stage import WorkshopPipelineStage


class WorkshopPipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="CDKWorkshopPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub(
                    "hurshd0/cdk-workshop-app",
                    "main",
                    authentication=cdk.SecretValue.secrets_manager("GithubToken"),
                ),
                commands=[
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth",
                    "pytest",
                ],
            ),
        )
