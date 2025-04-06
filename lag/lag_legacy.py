from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_apigateway as _api,
    aws_certificatemanager as _acm,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_logs as _logs,
    aws_route53 as _route53,
    aws_route53_targets as _r53targets,
    aws_ssm as _ssm
)

from constructs import Construct

class LagLegacy(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        region = Stack.of(self).region

        if region == 'ap-southeast-7':
            short = 'apse7'
        elif region == 'mx-central-1':
            short = 'mxc1'
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
            ]
        )

        acmprod = _acm.Certificate(
            self, 'acmprod',
            domain_name = short+'.lag.4n6ir.com',
            validation = _acm.CertificateValidation.from_dns(hostzone),
            subject_alternative_names = [
                'ipv4.'+short+'.lag.4n6ir.com',
                'ipv6.'+short+'.lag.4n6ir.com'
            ]
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

        int4test = _api.LambdaIntegration(
            region,
            proxy = True, 
            integration_responses = [
                _api.IntegrationResponse(
                    status_code = '200',
                    response_parameters = {
                        'method.response.header.Access-Control-Allow-Origin': "'*'"
                    }
                )
            ]
        )

        int4prod = _api.LambdaIntegration(
            region,
            proxy = True, 
            integration_responses = [
                _api.IntegrationResponse(
                    status_code = '200',
                    response_parameters = {
                        'method.response.header.Access-Control-Allow-Origin': "'*'"
                    }
                )
            ]
        )

        int6test = _api.LambdaIntegration(
            region,
            proxy = True, 
            integration_responses = [
                _api.IntegrationResponse(
                    status_code = '200',
                    response_parameters = {
                        'method.response.header.Access-Control-Allow-Origin': "'*'"
                    }
                )
            ]
        )

        int6prod = _api.LambdaIntegration(
            region,
            proxy = True, 
            integration_responses = [
                _api.IntegrationResponse(
                    status_code = '200',
                    response_parameters = {
                        'method.response.header.Access-Control-Allow-Origin': "'*'"
                    }
                )
            ]
        )

    ### API GATEWAYS ###

        api4test = _api.RestApi(
            self, 'api4test',
            endpoint_types = [
                _api.EndpointType.REGIONAL
            ]
        )

        api4test.root.add_method(
            'GET',
            int4test,
            method_responses = [
                _api.MethodResponse(
                    status_code = '200',
                    response_parameters = {
                        'method.response.header.Access-Control-Allow-Origin': True
                    }
                )
            ]
        )

        api4prod = _api.RestApi(
            self, 'api4prod',
            endpoint_types = [
                _api.EndpointType.REGIONAL
            ]
        )

        api4prod.root.add_method(
            'GET',
            int4prod,
            method_responses = [
                _api.MethodResponse(
                    status_code = '200',
                    response_parameters = {
                        'method.response.header.Access-Control-Allow-Origin': True
                    }
                )
            ]
        )

        api6test = _api.RestApi(
            self, 'api6test',
            endpoint_types = [
                _api.EndpointType.REGIONAL
            ]
        )

        api6test.root.add_method(
            'GET',
            int6test,
            method_responses = [
                _api.MethodResponse(
                    status_code = '200',
                    response_parameters = {
                        'method.response.header.Access-Control-Allow-Origin': True
                    }
                )
            ]
        )

        api6prod = _api.RestApi(
            self, 'api6prod',
            endpoint_types = [
                _api.EndpointType.REGIONAL
            ]
        )

        api6prod.root.add_method(
            'GET',
            int6prod,
            method_responses = [
                _api.MethodResponse(
                    status_code = '200',
                    response_parameters = {
                        'method.response.header.Access-Control-Allow-Origin': True
                    }
                )
            ]
        )

    ### BASE PATH MAPPINGS ###

        base4test = _api.BasePathMapping(
            self, 'base4test',
            domain_name = ipv4test,
            rest_api = api4test
        )

        base4prod = _api.BasePathMapping(
            self, 'base4prod',
            domain_name = ipv4prod,
            rest_api = api4prod
        )

        base6test = _api.BasePathMapping(
            self, 'base6test',
            domain_name = ipv6test,
            rest_api = api6test
        )

        base6prod = _api.BasePathMapping(
            self, 'base6prod',
            domain_name = ipv6prod,
            rest_api = api6prod
        )

    ### DNS RECORDS ###

        dns4test = _route53.ARecord(
            self, 'dns4test',
            zone = hostzone,
            record_name = 'ipv4.'+short+'.dev.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.ApiGatewayDomain(ipv4test)
            )
        )

        dns4prod = _route53.ARecord(
            self, 'dns4prod',
            zone = hostzone,
            record_name = 'ipv4.'+short+'.lag.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.ApiGatewayDomain(ipv4prod)
            )
        )

        dns6test = _route53.AaaaRecord(
            self, 'dns6test',
            zone = hostzone,
            record_name = 'ipv6.'+short+'.dev.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.ApiGatewayDomain(ipv6test)
            )
        )

        dns6prod = _route53.AaaaRecord(
            self, 'dns6prod',
            zone = hostzone,
            record_name = 'ipv6.'+short+'.lag.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.ApiGatewayDomain(ipv6prod)
            )
        )
