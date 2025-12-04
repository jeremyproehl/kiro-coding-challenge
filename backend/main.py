import os
import boto3
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from mangum import Mangum

app = FastAPI(title="Kiro Coding Challenge API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DynamoDB setup
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('EVENTS_TABLE_NAME', 'EventsTable')
table = dynamodb.Table(table_name)

# Pydantic models
class Event(BaseModel):
    eventId: str
    title: str
    description: str
    date: str
    location: str
    capacity: int
    organizer: str
    status: str = Field(default="active")

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    location: Optional[str] = None
    capacity: Optional[int] = None
    organizer: Optional[str] = None
    status: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to Kiro Coding Challenge API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/events")
def get_events(status: Optional[str] = Query(None)):
    try:
        if status:
            response = table.scan(
                FilterExpression='#status = :status',
                ExpressionAttributeNames={'#status': 'status'},
                ExpressionAttributeValues={':status': status}
            )
        else:
            response = table.scan()
        
        return response.get('Items', [])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving events: {str(e)}")

@app.get("/events/{event_id}")
def get_event(event_id: str):
    try:
        response = table.get_item(Key={'eventId': event_id})
        
        if 'Item' not in response:
            raise HTTPException(status_code=404, detail="Event not found")
        
        return response['Item']
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving event: {str(e)}")

@app.post("/events", status_code=201)
def create_event(event: Event):
    try:
        # Check if event already exists
        response = table.get_item(Key={'eventId': event.eventId})
        if 'Item' in response:
            raise HTTPException(status_code=409, detail="Event already exists")
        
        # Store event in DynamoDB
        table.put_item(Item=event.dict())
        
        return {"eventId": event.eventId}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating event: {str(e)}")

@app.put("/events/{event_id}")
def update_event(event_id: str, event_update: EventUpdate):
    try:
        # Check if event exists
        response = table.get_item(Key={'eventId': event_id})
        if 'Item' not in response:
            raise HTTPException(status_code=404, detail="Event not found")
        
        # Build update expression
        update_data = {k: v for k, v in event_update.dict().items() if v is not None}
        
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")
        
        update_expression = "SET " + ", ".join([f"#{k} = :{k}" for k in update_data.keys()])
        expression_attribute_names = {f"#{k}": k for k in update_data.keys()}
        expression_attribute_values = {f":{k}": v for k, v in update_data.items()}
        
        table.update_item(
            Key={'eventId': event_id},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )
        
        # Return updated event
        response = table.get_item(Key={'eventId': event_id})
        return response['Item']
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating event: {str(e)}")

@app.delete("/events/{event_id}")
def delete_event(event_id: str):
    try:
        # Check if event exists
        response = table.get_item(Key={'eventId': event_id})
        if 'Item' not in response:
            raise HTTPException(status_code=404, detail="Event not found")
        
        table.delete_item(Key={'eventId': event_id})
        
        return {"message": "Event deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting event: {str(e)}")

# Lambda handler
handler = Mangum(app)
