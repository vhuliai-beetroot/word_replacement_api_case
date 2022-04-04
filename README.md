# Word replacement API case

## Project structure

Project is generated using AWS cdk via `cdk init --language typescript` and has respectful template structure.

You may find IaC inside for this API case inside `lib` folder and service which will be shipped to AWS located in `src` folder. 

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template


## Deploy the project

1. Configure AWS cdk locally (See https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-typescript.html).
2. Export required environment variable `WR_JWK4JWT` (See additional documentation from service [src](src/README.md)).
3. Check configurations via `cdk synth`.
4. Deploy the stack to AWS via `cdk deploy`.
5. Remove deployed infrastructure via `cdk destroy`. 
