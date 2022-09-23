#!/usr/bin/env python

from cdktf_cdktf_provider_aws import AwsProvider, s3
from cdktf import App, NamedRemoteWorkspace, TerraformStack, TerraformOutput, RemoteBackend
from constructs import Construct
BUCKET_NAME = "<< THE UNIQUE NAME FOR MY S3 BUCKET >>"
TFCLOUD_ORGA = "<< THE NAME OF MY ORGANIZATION >>"


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region="eu-west-1")

        bucket = s3.S3Bucket(self, "cdktf-test",
                             bucket=BUCKET_NAME)

        TerraformOutput(self, "s3_arn",
                        value=bucket.arn,
                        )


app = App()
stack = MyStack(app, "cdktf_test")
RemoteBackend(stack,
              hostname='app.terraform.io',
              organization=TFCLOUD_ORGA,
              workspaces=NamedRemoteWorkspace('test_cdktf')
              )

app.synth()
