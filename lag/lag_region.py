from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_apigatewayv2 as _api,
    aws_apigatewayv2_integrations as _integrations,
    aws_certificatemanager as _acm,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_logs as _logs,
    aws_route53 as _route53,
    aws_route53_targets as _r53targets,
    aws_ssm as _ssm
)

from constructs import Construct

class LagRegion(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        region = Stack.of(self).region

        if region == 'af-south-1':
            short = 'afs1'
        elif region == 'ap-east-1':
            short = 'ape1'
        elif region == 'ap-northeast-1':
            short = 'apne1'
        elif region == 'ap-northeast-2':
            short = 'apne2'
        elif region == 'ap-northeast-3':
            short = 'apne3'
        elif region == 'ap-south-1':
            short = 'aps1'
        elif region == 'ap-south-2':
            short = 'aps2'
        elif region == 'ap-southeast-1':
            short = 'apse1'
        elif region == 'ap-southeast-2':
            short = 'apse2'
        elif region == 'ap-southeast-3':
            short = 'apse3'
        elif region == 'ap-southeast-4':
            short = 'apse4'
        elif region == 'ap-southeast-5':
            short = 'apse5'
        elif region == 'ca-central-1':
            short = 'cac1'
        elif region == 'ca-west-1':
            short = 'caw1'
        elif region == 'eu-central-1':
            short = 'euc1'
        elif region == 'eu-central-2':
            short = 'euc2'
        elif region == 'eu-north-1':
            short = 'eun1'
        elif region == 'eu-south-1':
            short = 'eus1'
        elif region == 'eu-south-2':
            short = 'eus2'
        elif region == 'eu-west-1':
            short = 'euw1'
        elif region == 'eu-west-2':
            short = 'euw2'
        elif region == 'eu-west-3':
            short = 'euw3'
        elif region == 'il-central-1':
            short = 'ilc1'
        elif region == 'me-central-1':
            short = 'mec1'
        elif region == 'me-south-1':
            short = 'mes1'
        elif region == 'sa-east-1':
            short = 'sae1'
        elif region == 'us-east-1':
            short = 'use1'
        elif region == 'us-east-2':
            short = 'use2'
        elif region == 'us-west-1':
            short = 'usw1'
        elif region == 'us-west-2':
            short = 'usw2'
        else:
            raise ValueError(f"Unsupported Region: {region}")

    ### IAM ROLE ###

        role = _iam.Role(
            self, 'role',
            assumed_by = _iam.ServicePrincipal(
                'lambda.amazonaws.com'
            )
        )

        role.add_managed_policy(
            _iam.ManagedPolicy.from_aws_managed_policy_name(
                'service-role/AWSLambdaBasicExecutionRole'
            )
        )

        role.add_to_policy(
            _iam.PolicyStatement(
                actions = [
                    'apigateway:GET'
                ],
                resources = [
                    '*'
                ]
            )
        )

    ### LAMBDA FUNCTION ###

        region = _lambda.Function(
            self, 'region',
            runtime = _lambda.Runtime.PYTHON_3_13,
            architecture = _lambda.Architecture.ARM_64,
            code = _lambda.Code.from_asset('region'),
            handler = 'region.handler',
            timeout = Duration.seconds(7),
            memory_size = 128,
            role = role
        )

        logs = _logs.LogGroup(
            self, 'logs',
            log_group_name = '/aws/lambda/'+region.function_name,
            retention = _logs.RetentionDays.THIRTEEN_MONTHS,
            removal_policy = RemovalPolicy.DESTROY
        )

    ### HOSTZONE ###

        hostzoneid = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'hostzoneid',
            parameter_name = '/network/hostzone'
        )

        hostzone = _route53.HostedZone.from_hosted_zone_attributes(
             self, 'hostzone',
             hosted_zone_id = hostzoneid.string_value,
             zone_name = '4n6ir.com'
        ) 

    ### ACM CERTIFICATE ###

        acmtest = _acm.Certificate(
            self, 'acmtest',
            domain_name = short+'.dev.4n6ir.com',
            validation = _acm.CertificateValidation.from_dns(hostzone),
            subject_alternative_names = [
                'ipv4.'+short+'.dev.4n6ir.com',
                'ipv6.'+short+'.dev.4n6ir.com'
            ],
        )

        acmprod = _acm.Certificate(
            self, 'acmprod',
            domain_name = short+'.lag.4n6ir.com',
            validation = _acm.CertificateValidation.from_dns(hostzone),
            subject_alternative_names = [
                'ipv4.'+short+'.lag.4n6ir.com',
                'ipv6.'+short+'.lag.4n6ir.com'
            ],
        )

    ### DOMAIN NAMES ###

        ipv4test = _api.DomainName(
            self, 'ipv4test',
            domain_name = 'ipv4.'+short+'.dev.4n6ir.com',
            certificate = acmtest
        )

        ipv4prod = _api.DomainName(
            self, 'ipv4prod',
            domain_name = 'ipv4.'+short+'.lag.4n6ir.com',
            certificate = acmprod
        )

        ipv6test = _api.DomainName(
            self, 'ipv6test',
            domain_name = 'ipv6.'+short+'.dev.4n6ir.com',
            certificate = acmtest
        )

        ipv6prod = _api.DomainName(
            self, 'ipv6prod',
            domain_name = 'ipv6.'+short+'.lag.4n6ir.com',
            certificate = acmprod
        )

    ### API INTEGRATIONS ###

        int4test = _integrations.HttpLambdaIntegration(
            'int4test', region
        )

        int4prod = _integrations.HttpLambdaIntegration(
            'int4prod', region
        )

        int6test = _integrations.HttpLambdaIntegration(
            'int6test', region
        )

        int6prod = _integrations.HttpLambdaIntegration(
            'int6prod', region
        )

    ### API GATEWAYS ###

        api4test = _api.HttpApi(
            self, 'api4test',
            default_domain_mapping = _api.DomainMappingOptions(
                domain_name = ipv4test
            )
        )

        api4test.add_routes(
            path = '/',
            methods = [
                _api.HttpMethod.GET
            ],
            integration = int4test
        )

        api4prod = _api.HttpApi(
            self, 'api4prod',
            default_domain_mapping = _api.DomainMappingOptions(
                domain_name = ipv4prod
            )
        )

        api4prod.add_routes(
            path = '/',
            methods = [
                _api.HttpMethod.GET
            ],
            integration = int4prod
        )

        api6test = _api.HttpApi(
            self, 'api6test',
            default_domain_mapping = _api.DomainMappingOptions(
                domain_name = ipv6test
            )
        )

        api6test.add_routes(
            path = '/',
            methods = [
                _api.HttpMethod.GET
            ],
            integration = int6test
        )

        api6prod = _api.HttpApi(
            self, 'api6prod',
            default_domain_mapping = _api.DomainMappingOptions(
                domain_name = ipv6prod
            )
        )

        api6prod.add_routes(
            path = '/',
            methods = [
                _api.HttpMethod.GET
            ],
            integration = int6prod
        )

    ### DNS RECORDS ###

        dns4test = _route53.ARecord(
            self, 'dns4test',
            zone = hostzone,
            record_name = 'ipv4.'+short+'.dev.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.ApiGatewayv2DomainProperties(
                    ipv4test.regional_domain_name,
                    ipv4test.regional_hosted_zone_id
                )
            )
        )

        dns4prod = _route53.ARecord(
            self, 'dns4prod',
            zone = hostzone,
            record_name = 'ipv4.'+short+'.lag.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.ApiGatewayv2DomainProperties(
                    ipv4prod.regional_domain_name,
                    ipv4prod.regional_hosted_zone_id
                )
            )
        )

        dns6test = _route53.AaaaRecord(
            self, 'dns6test',
            zone = hostzone,
            record_name = 'ipv6.'+short+'.dev.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.ApiGatewayv2DomainProperties(
                    ipv6test.regional_domain_name,
                    ipv6test.regional_hosted_zone_id
                )
            )
        )

        dns6prod = _route53.AaaaRecord(
            self, 'dns6prod',
            zone = hostzone,
            record_name = 'ipv6.'+short+'.lag.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.ApiGatewayv2DomainProperties(
                    ipv6prod.regional_domain_name,
                    ipv6prod.regional_hosted_zone_id
                )
            )
        )
