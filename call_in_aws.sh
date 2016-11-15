#!/bin/bash -ex

ARN=$1
PROFILE=$2
aws lambda invoke --function-name $ARN --log-type Tail --payload '{}' --profile $PROFILE output.txt | jq -r .LogResult | base64 --decode
