#!/bin/bash
# Bundle Lambda function with dependencies

set -e

BUNDLE_DIR="lambda_bundle"

echo "Creating bundle directory..."
rm -rf $BUNDLE_DIR
mkdir -p $BUNDLE_DIR

echo "Installing dependencies..."
pip3 install -r requirements.txt -t $BUNDLE_DIR --platform manylinux2014_x86_64 --only-binary=:all: --python-version 3.11

echo "Copying application code..."
cp main.py $BUNDLE_DIR/

echo "Bundle created successfully in $BUNDLE_DIR/"
ls -lh $BUNDLE_DIR/
