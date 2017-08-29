#!/bin/bash


#config in .s3_website.yaml

echo ${AWS_ACCESS_KEY_ID?"Need to set STATE"}
echo ${AWS_SECRET_ACCESS_KEY?"Need to set STATE"}
s3-deploy-website


