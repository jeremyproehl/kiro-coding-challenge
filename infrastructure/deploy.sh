#!/bin/bash

source .env

echo "Installing Python dependencies..."
venv/bin/pip install -q -r requirements.txt

echo "Synthesizing CDK stack..."
/opt/homebrew/bin/cdk synth

echo "Bootstrapping CDK (if needed)..."
/opt/homebrew/bin/cdk bootstrap

echo "Deploying stack..."
/opt/homebrew/bin/cdk deploy --require-approval never --outputs-file outputs.json
