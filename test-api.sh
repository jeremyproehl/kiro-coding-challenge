#!/bin/bash

API_URL="https://2gw8nqdwla.execute-api.us-west-2.amazonaws.com/prod"

echo "Testing API endpoints..."
echo ""

echo "1. Testing root endpoint:"
curl -s "$API_URL/" | python3 -m json.tool
echo ""

echo "2. Testing health endpoint:"
curl -s "$API_URL/health" | python3 -m json.tool
echo ""

echo "3. Testing events endpoint:"
curl -s "$API_URL/events" | python3 -m json.tool
echo ""
