# Events Management API

A serverless REST API for managing events, built with FastAPI and deployed on AWS using Lambda, API Gateway, and DynamoDB.

## 🚀 Live API

**Base URL**: `https://2gw8nqdwla.execute-api.us-west-2.amazonaws.com/prod/`

## 📋 Features

- **CRUD Operations**: Create, Read, Update, and Delete events
- **Filtering**: Query events by status
- **Serverless Architecture**: Built on AWS Lambda for scalability and cost-efficiency
- **NoSQL Storage**: DynamoDB for fast, flexible data storage
- **Input Validation**: Pydantic models for request validation
- **CORS Enabled**: Ready for web application integration

## 🏗️ Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐      ┌──────────────┐
│   Client    │─────▶│ API Gateway  │─────▶│   Lambda    │─────▶│  DynamoDB    │
│             │◀─────│              │◀─────│  (FastAPI)  │◀─────│              │
└─────────────┘      └──────────────┘      └─────────────┘      └──────────────┘
```

## 📁 Project Structure

```
.
├── backend/              # FastAPI application
│   ├── main.py          # API endpoints and business logic
│   ├── requirements.txt # Python dependencies
│   ├── bundle.sh        # Lambda bundling script
│   └── docs/            # API documentation (generated)
├── infrastructure/       # AWS CDK Infrastructure as Code
│   ├── app.py           # CDK app entry point
│   ├── stacks/
│   │   └── backend_stack.py  # Stack definition
│   └── requirements.txt
└── test_deployment.py   # API test suite
```

## 🔧 Setup & Development

### Prerequisites

- Python 3.11+
- Node.js (for AWS CDK)
- AWS CLI configured with credentials
- pip

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd kiro-coding-challenge
   ```

2. **Set up backend**
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run locally**
   ```bash
   uvicorn main:app --reload
   ```
   API will be available at `http://localhost:8000`
   Interactive docs at `http://localhost:8000/docs`

### Deployment

1. **Install CDK dependencies**
   ```bash
   cd infrastructure
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   npm install -g aws-cdk
   ```

2. **Bundle Lambda dependencies**
   ```bash
   cd ../backend
   bash bundle.sh
   ```

3. **Deploy to AWS**
   ```bash
   cd ../infrastructure
   cdk bootstrap  # First time only
   cdk deploy
   ```

## 📚 API Documentation

### Event Schema

```json
{
  "eventId": "string",
  "title": "string",
  "description": "string",
  "date": "string",
  "location": "string",
  "capacity": integer,
  "organizer": "string",
  "status": "string"
}
```

### Endpoints

#### Get All Events
```http
GET /events
```
**Query Parameters:**
- `status` (optional): Filter by event status (e.g., "active")

**Response:** `200 OK`
```json
[
  {
    "eventId": "event-123",
    "title": "Tech Conference 2024",
    "description": "Annual technology conference",
    "date": "2024-12-15",
    "location": "San Francisco",
    "capacity": 500,
    "organizer": "Tech Corp",
    "status": "active"
  }
]
```

#### Get Event by ID
```http
GET /events/{eventId}
```
**Response:** `200 OK` or `404 Not Found`

#### Create Event
```http
POST /events
Content-Type: application/json

{
  "eventId": "event-123",
  "title": "Tech Conference 2024",
  "description": "Annual technology conference",
  "date": "2024-12-15",
  "location": "San Francisco",
  "capacity": 500,
  "organizer": "Tech Corp",
  "status": "active"
}
```
**Response:** `201 Created` or `409 Conflict` (if event exists)

#### Update Event
```http
PUT /events/{eventId}
Content-Type: application/json

{
  "title": "Updated Title",
  "capacity": 600
}
```
**Response:** `200 OK` or `404 Not Found`

#### Delete Event
```http
DELETE /events/{eventId}
```
**Response:** `200 OK` or `404 Not Found`

## 🧪 Testing

Run the test suite:
```bash
python3 test_deployment.py
```

All tests validate:
- ✅ Listing all events
- ✅ Filtering events by status
- ✅ Creating new events
- ✅ Retrieving specific events
- ✅ Updating events
- ✅ Deleting events

## 🛠️ Technologies

- **Backend**: FastAPI, Pydantic, Boto3, Mangum
- **Infrastructure**: AWS CDK (Python)
- **AWS Services**: Lambda, API Gateway, DynamoDB, IAM
- **Runtime**: Python 3.11

## 📝 Notes

- DynamoDB reserved keywords (`status`, `capacity`) are handled using ExpressionAttributeNames
- CORS is enabled for all origins (configure for production use)
- Lambda function has 30-second timeout and 512MB memory
- DynamoDB uses on-demand billing mode

## 📄 License

This project is part of the Kiro Coding Challenge.
