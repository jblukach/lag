# lag

Lag provides the global infrastructure to measure network latency between source and AWS Cloud regions.

The testing endpoint uses a regional HTTP API Gateway, except for Mexico (mx-central-1) and Thailand (ap-southeast-7), where only a REST API Gateway is available, with a Lambda returning the results.

The CloudFront configuration uses all edge locations, with a Function returning the source address from the closest geolocation.

All three endpoints support IPv4 and IPv6 addresses, which [Laggy](https://github.com/jblukach/laggy) uses to measure network latency and jitter between the source and AWS Cloud regions.