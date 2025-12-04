from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    RemovalPolicy,
    Duration,
    CfnOutput
)
from constructs import Construct
import os

class BackendStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # DynamoDB Table
        events_table = dynamodb.Table(
            self, "EventsTable",
            partition_key=dynamodb.Attribute(
                name="eventId",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY
        )
        
        # Lambda Function with pre-bundled dependencies
        # Dependencies are bundled using backend/bundle.sh script
        backend_bundle_path = os.path.join(os.path.dirname(__file__), "../../backend/lambda_bundle")
        
        api_lambda = lambda_.Function(
            self, "EventsApiFunction",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="main.handler",
            code=lambda_.Code.from_asset(backend_bundle_path),
            environment={
                "EVENTS_TABLE_NAME": events_table.table_name
            },
            timeout=Duration.seconds(30),
            memory_size=512
        )
        
        # Grant Lambda permissions to access DynamoDB
        events_table.grant_read_write_data(api_lambda)
        
        # API Gateway
        api = apigateway.LambdaRestApi(
            self, "EventsApi",
            handler=api_lambda,
            proxy=True,
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=apigateway.Cors.ALL_METHODS,
                allow_headers=["*"]
            )
        )
        
        # Outputs
        CfnOutput(
            self, "ApiUrl",
            value=api.url,
            description="API Gateway URL"
        )
        
        CfnOutput(
            self, "TableName",
            value=events_table.table_name,
            description="DynamoDB Table Name"
        )
