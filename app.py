#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lag.lag_legacy import LagLegacy
from lag.lag_region import LagRegion

app = cdk.App()

LagRegion(
    app, 'LagRegion-af-south-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'af-south-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-east-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-east-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-northeast-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-northeast-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-northeast-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-northeast-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-northeast-3',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-northeast-3'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-south-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-south-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-south-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-south-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-southeast-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-southeast-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-southeast-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-southeast-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-southeast-3',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-southeast-3'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-southeast-4',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-southeast-4'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ap-southeast-5',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-southeast-5'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagLegacy(
    app, 'LagLegacy-ap-southeast-7',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ap-southeast-7'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ca-central-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ca-central-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-ca-west-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'ca-west-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-eu-central-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'eu-central-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-eu-central-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'eu-central-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-eu-north-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'eu-north-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-eu-south-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'eu-south-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-eu-south-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'eu-south-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-eu-west-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'eu-west-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-eu-west-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'eu-west-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-eu-west-3',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'eu-west-3'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-il-central-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'il-central-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-me-central-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'me-central-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-me-south-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'me-south-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagLegacy(
    app, 'LagLegacy-mx-central-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'mx-central-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-sa-east-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'sa-east-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-us-east-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-us-east-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-us-west-1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

LagRegion(
    app, 'LagRegion-us-west-2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

cdk.Tags.of(app).add('Alias','4n6ir.com')
cdk.Tags.of(app).add('GitHub','https://github.com/jblukach/lag')

app.synth()