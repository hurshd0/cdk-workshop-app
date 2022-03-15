from constructs import Construct
from aws_cdk import aws_lambda as _lambda, aws_dynamodb as ddb


class HitCounter(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        downstream: _lambda.IFunction,
        read_capacity: int = 5,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        if read_capacity < 5 or read_capacity > 20:
            raise ValueError("read_capacity must be between 5 and 20")

        self._table = ddb.Table(
            self,
            "Hits",
            partition_key={"name": "path", "type": ddb.AttributeType.STRING},
            encryption=ddb.TableEncryption.AWS_MANAGED,
            read_capacity=read_capacity,
        )

        self._handler = _lambda.Function(
            self,
            "HitCountHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="hitcount.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "DOWNSTREAM_FUNCTION_NAME": downstream.function_name,
                "HITS_TABLE_NAME": self._table.table_name,
            },
        )

        self._table.grant_read_write_data(self._handler)
        downstream.grant_invoke(self._handler)

    @property
    def handler(self):
        return self._handler

    @property
    def table(self):
        return self._table
