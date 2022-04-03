import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Duration } from "aws-cdk-lib";
import * as iam from "aws-cdk-lib/aws-iam";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as ecs from "aws-cdk-lib/aws-ecs";
import * as ecs_patterns from "aws-cdk-lib/aws-ecs-patterns";

export class WordReplacementApiCaseStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "WordReplacementVpc", {
      maxAzs: 3
    });
    
    const cluster = new ecs.Cluster(this, "WordReplacementCluster", {
      vpc: vpc
    });

    const logging = new ecs.AwsLogDriver({
      streamPrefix: "WordReplacementLogs"
    });

    const taskRole = new iam.Role(this, `ecs-taskRole-${this.stackName}`, {
      roleName: `ecs-taskRole-${this.stackName}`,
      assumedBy: new iam.ServicePrincipal('ecs-tasks.amazonaws.com')
    });

    const executionRolePolicy =  new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      resources: ['*'],
      actions: [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ]
    });

    const taskDef = new ecs.FargateTaskDefinition(this, "WordReplacement-taskdef", {
      taskRole: taskRole
    });

    taskDef.addToExecutionRolePolicy(executionRolePolicy);

    const appJWK4JWT = process.env.WR_JWK4JWT || '<not-a-secret>';

    const container = taskDef.addContainer('word-replacement-app', {
      image: ecs.ContainerImage.fromAsset("src/"),
      memoryLimitMiB: 512,
      cpu: 256,
      environment: {
        WR_JWK4JWT: appJWK4JWT,
      },
      logging
    });


    container.addPortMappings({
      containerPort: 8000,
      protocol: ecs.Protocol.TCP
    });

    const fargateService = new ecs_patterns.ApplicationLoadBalancedFargateService(this, "WordReplacementFargateService", {
      cluster: cluster,
      taskDefinition: taskDef,
      publicLoadBalancer: true,
      desiredCount: 1,
      listenerPort: 80
    });

    fargateService.targetGroup.configureHealthCheck({
      path: "/health",
    });

    const scaling = fargateService.service.autoScaleTaskCount({ maxCapacity: 3 });
    scaling.scaleOnCpuUtilization("CpuScaling", {
      targetUtilizationPercent: 10,
      scaleInCooldown: Duration.seconds(60),
      scaleOutCooldown: Duration.seconds(60)
    });

  }
}
