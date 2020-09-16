#!/bin/bash

python -m venv ./venv

autorest \
    --input-file:/input/saasapi.v2.json \
    --v3 \
    --python \
    --output-folder:/out  \
    --add-credentials \
    --namespace:com.microsoft.marketplace.saas \
    --verbose \
    --clear-output-folder:true \
    --public-clients:true \
    --license-header:MICROSOFT_MIT_NO_VERSION

#--use:@autorest/python@5.3.2 \

#autorest \
#    --input-file:/input/meteringapi.v1.json \
#    --v3 \
#    --python \
#    --use:@autorest/python@5.3.2 \
#    --output-folder:/out  \
#    --add-credentials \
#    --namespace:com.microsoft.marketplace.meter \
#    --verbose \
#    --clear-output-folder:true \
#    --public-clients:true \
#    --license-header:MICROSOFT_MIT_NO_VERSION
