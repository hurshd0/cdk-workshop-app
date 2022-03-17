from constructs import Construct
from aws_cdk import Stack
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
import aws_cdk as cdk
from .pipeline_stage import WorkshopPipelineStage


class WorkshopPipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        source = CodePipelineSource.git_hub(
            "hurshd0/cdk-workshop-app",
            "main",
            authentication=cdk.SecretValue.secrets_manager("GithubToken"),
        )

        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="CDKWorkshopPipeline",
            synth=ShellStep(
                "Synth",
                input=source,
                commands=["scripts/build.sh"],
            ),
        )

        testing = WorkshopPipelineStage(self, "Testing")
        testing_stage = pipeline.add_stage(testing)
        testing_stage.add_post(
            ShellStep(
                "Validate",
                input=source,
                commands=["pip install -r requirements.txt", "pytest"],
            )
        )
