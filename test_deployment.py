#!/usr/bin/env python3
"""
Test script for the Events API deployment
"""
import requests
import json
import sys

API_URL = "https://2gw8nqdwla.execute-api.us-west-2.amazonaws.com/prod"

def test_endpoint(method, path, expected_status, data=None, description=""):
    """Test an API endpoint"""
    url = f"{API_URL}{path}"
    print(f"\n{'='*60}")
    print(f"TEST: {description}")
    print(f"{'='*60}")
    print(f"{method} {url}")
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            print(f"Request Body: {json.dumps(data, indent=2)}")
            response = requests.post(url, json=data)
        elif method == "PUT":
            print(f"Request Body: {json.dumps(data, indent=2)}")
            response = requests.put(url, json=data)
        elif method == "DELETE":
            response = requests.delete(url)
        
        print(f"\nStatus Code: {response.status_code}")
        print(f"Expected: {expected_status}")
        
        try:
            response_data = response.json()
            print(f"Response: {json.dumps(response_data, indent=2)}")
        except:
            print(f"Response: {response.text}")
        
        if response.status_code == expected_status:
            print("✅ PASS")
            return True
        else:
            print("❌ FAIL")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    print("="*60)
    print("EVENTS API DEPLOYMENT TEST")
    print("="*60)
    
    results = []
    
    # Test 1: GET /events
    results.append(test_endpoint(
        "GET", "/events", 200,
        description="Get all events"
    ))
    
    # Test 2: GET /events?status=active
    results.append(test_endpoint(
        "GET", "/events?status=active", 200,
        description="Get events filtered by status"
    ))
    
    # Test 3: POST /events
    event_data = {
        "date": "2024-12-15",
        "eventId": "api-test-event-456",
        "organizer": "API Test Organizer",
        "description": "Testing API Gateway integration",
        "location": "API Test Location",
        "title": "API Gateway Test Event",
        "capacity": 200,
        "status": "active"
    }
    results.append(test_endpoint(
        "POST", "/events", 201, event_data,
        description="Create a new event"
    ))
    
    # Test 4: GET /events/{eventId}
    results.append(test_endpoint(
        "GET", "/events/api-test-event-456", 200,
        description="Get specific event by ID"
    ))
    
    # Test 5: PUT /events/{eventId}
    update_data = {
        "title": "Updated API Gateway Test Event",
        "capacity": 250
    }
    results.append(test_endpoint(
        "PUT", "/events/api-test-event-456", 200, update_data,
        description="Update an existing event"
    ))
    
    # Test 6: DELETE /events/{eventId}
    results.append(test_endpoint(
        "DELETE", "/events/api-test-event-456", 200,
        description="Delete an event"
    ))
    
    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✅ ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        sys.exit(1)

if __name__ == "__main__":
    main()
