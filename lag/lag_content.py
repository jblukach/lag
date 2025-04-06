from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_certificatemanager as _acm,
    aws_cloudfront as _cloudfront,
    aws_cloudfront_origins as _origins,
    aws_logs as _logs,
    aws_route53 as _route53,
    aws_route53_targets as _r53targets,
    aws_s3 as _s3,
    aws_s3_deployment as _deployment,
    aws_ssm as _ssm
)

from constructs import Construct

class LagContent(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    ### CLOUD WATCH ###

        logs = _logs.LogGroup(
            self, 'logs',
            log_group_name = '/aws/cloudfront/whoami',
            retention = _logs.RetentionDays.THIRTEEN_MONTHS,
            removal_policy = RemovalPolicy.DESTROY
        )

        lagipv4logs = _logs.LogGroup(
            self, 'lagipv4logs',
            log_group_name = '/aws/cloudfront/lag/ipv4',
            retention = _logs.RetentionDays.THIRTEEN_MONTHS,
            removal_policy = RemovalPolicy.DESTROY
        )

        lagipv6logs = _logs.LogGroup(
            self, 'lagipv6logs',
            log_group_name = '/aws/cloudfront/lag/ipv6',
            retention = _logs.RetentionDays.THIRTEEN_MONTHS,
            removal_policy = RemovalPolicy.DESTROY
        )

    ### S3 BUCKET ###

        bucket = _s3.Bucket(
            self, 'bucket',
            encryption = _s3.BucketEncryption.S3_MANAGED,
            block_public_access = _s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects = True,
            enforce_ssl = True,
            versioned = False
        )

        deployment = _deployment.BucketDeployment(
            self, 'deployment',
            sources = [
                _deployment.Source.asset('html')
            ],
            destination_bucket = bucket,
            prune = False
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

        acm = _acm.Certificate(
            self, 'acm',
            domain_name = 'whoami.4n6ir.com',
            validation = _acm.CertificateValidation.from_dns(hostzone)
        )

        lagacm = _acm.Certificate(
            self, 'lagacm',
            domain_name = 'lag.4n6ir.com',
            validation = _acm.CertificateValidation.from_dns(hostzone),
            subject_alternative_names = [
                'ipv4.lag.4n6ir.com',
                'ipv6.lag.4n6ir.com'
            ]
        )

    ### CLOUDFRONT FUNCTIONS ###

        function = _cloudfront.Function(
            self, 'function',
            code = _cloudfront.FunctionCode.from_file(
                file_path = 'whoami/whoami.js'
            ),
            runtime = _cloudfront.FunctionRuntime.JS_2_0
        )

    ### CLOUDFRONT DISTRIBUTIONS ###

        distribution = _cloudfront.Distribution(
            self, 'distribution',
            comment = 'whoami.4n6ir.com',
            default_behavior = _cloudfront.BehaviorOptions(
                origin = _origins.S3BucketOrigin.with_origin_access_control(bucket),
                viewer_protocol_policy = _cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                cache_policy = _cloudfront.CachePolicy.CACHING_DISABLED,
                function_associations = [
                    _cloudfront.FunctionAssociation(
                        function = function,
                        event_type = _cloudfront.FunctionEventType.VIEWER_REQUEST
                    )   
                ]
            ),
            domain_names = [
                'whoami.4n6ir.com'
            ],
            error_responses = [
                _cloudfront.ErrorResponse(
                    http_status = 404,
                    response_http_status = 200,
                    response_page_path = '/'
                )
            ],
            minimum_protocol_version = _cloudfront.SecurityPolicyProtocol.TLS_V1_2_2021,
            price_class = _cloudfront.PriceClass.PRICE_CLASS_ALL,
            http_version = _cloudfront.HttpVersion.HTTP2_AND_3,
            enable_ipv6 = True,
            certificate = acm
        )

        lagipv4dist = _cloudfront.Distribution(
            self, 'lagipv4dist',
            comment = 'ipv4.lag.4n6ir.com',
            default_root_object = 'index-lag-ipv4.html',
            default_behavior = _cloudfront.BehaviorOptions(
                origin = _origins.S3BucketOrigin.with_origin_access_control(bucket),
                viewer_protocol_policy = _cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                #response_headers_policy = _cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                cache_policy = _cloudfront.CachePolicy.CACHING_DISABLED
            ),
            domain_names = [
                'ipv4.lag.4n6ir.com'
            ],
            error_responses = [
                _cloudfront.ErrorResponse(
                    http_status = 404,
                    response_http_status = 200,
                    response_page_path = '/'
                )
            ],
            minimum_protocol_version = _cloudfront.SecurityPolicyProtocol.TLS_V1_2_2021,
            price_class = _cloudfront.PriceClass.PRICE_CLASS_ALL,
            http_version = _cloudfront.HttpVersion.HTTP2_AND_3,
            enable_ipv6 = False,
            certificate = lagacm
        )

        lagipv6dist = _cloudfront.Distribution(
            self, 'lagipv6dist',
            comment = 'ipv6.lag.4n6ir.com',
            default_root_object = 'index-lag-ipv6.html',
            default_behavior = _cloudfront.BehaviorOptions(
                origin = _origins.S3BucketOrigin.with_origin_access_control(bucket),
                viewer_protocol_policy = _cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                #response_headers_policy = _cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                cache_policy = _cloudfront.CachePolicy.CACHING_DISABLED
            ),
            domain_names = [
                'ipv6.lag.4n6ir.com'
            ],
            error_responses = [
                _cloudfront.ErrorResponse(
                    http_status = 404,
                    response_http_status = 200,
                    response_page_path = '/'
                )
            ],
            minimum_protocol_version = _cloudfront.SecurityPolicyProtocol.TLS_V1_2_2021,
            price_class = _cloudfront.PriceClass.PRICE_CLASS_ALL,
            http_version = _cloudfront.HttpVersion.HTTP2_AND_3,
            enable_ipv6 = True,
            certificate = lagacm
        )

    ### ROUTE53 DNS ###

        ipv4dns = _route53.ARecord(
            self, 'ipv4dns',
            zone = hostzone,
            record_name = 'whoami.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.CloudFrontTarget(distribution)
            )
        )

        ipv6dns = _route53.AaaaRecord(
            self, 'ipv6dns',
            zone = hostzone,
            record_name = 'whoami.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.CloudFrontTarget(distribution)
            )
        )

        lagipv4dns = _route53.ARecord(
            self, 'lagipv4dns',
            zone = hostzone,
            record_name = 'ipv4.lag.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.CloudFrontTarget(lagipv4dist)
            )
        )

        lagipv6dns = _route53.AaaaRecord(
            self, 'lagipv6dns',
            zone = hostzone,
            record_name = 'ipv6.lag.4n6ir.com',
            target = _route53.RecordTarget.from_alias(
                _r53targets.CloudFrontTarget(lagipv6dist)
            )
        )
