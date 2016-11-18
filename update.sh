#!/bin/bash -xe

PROFILE=$1
[[ -z $PROFILE ]] && echo "Usage: $0 aws-profile-name" && exit 1

# update lambda
gordon build
AWS_PROFILE=$PROFILE gordon apply

# update s3 site
pipeline-scripts/cf_stack.py update alexa-word-of-the-day -f s3/s3-alexa-flash-briefing-site.yaml -a $PROFILE -r us-east-1
BUCKET=`aws cloudformation describe-stacks --stack-name alexa-word-of-the-day --profile $PROFILE --region us-east-1 | jq .Stacks[0].Outputs[0].OutputValue | sed -e "s/\"//g"`
cd s3/contents
aws s3 sync . s3://$BUCKET/ --profile $PROFILE --acl public-read
