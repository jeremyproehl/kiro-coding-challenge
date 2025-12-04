---
inclusion: fileMatch
fileMatchPattern: '**/*api*.py|**/main.py|**/*endpoint*.py|**/*route*.py'
---

# REST API Standards for Prototype Applications

This guide defines REST API conventions for small prototype applications. Follow these standards when working with API-related files.

## HTTP Methods

Use standard HTTP methods with their semantic meanings:

- **GET**: Retrieve resources (read-only, idempotent, cacheable)
- **POST**: Create new resources (non-idempotent)
- **PUT**: Update/replace entire resources (idempotent)
- **PATCH**: Partial update of resources (idempotent)
- **DELETE**: Remove resources (idempotent)

## HTTP Status Codes

### Success Codes (2xx)
- **200 OK**: Successful GET, PUT, PATCH, or DELETE
- **201 Created**: Successful POST that creates a resource
- **204 No Content**: Successful request with no response body (optional for DELETE)

### Client Error Codes (4xx)
- **400 Bad Request**: Invalid request format or validation error
- **404 Not Found**: Resource doesn't exist
- **409 Conflict**: Resource already exists or conflict with current state
- **422 Unprocessable Entity**: Valid format but semantic errors

### Server Error Codes (5xx)
- **500 Internal Server Error**: Unexpected server error
- **502 Bad Gateway**: Invalid response from upstream service
- **503 Service Unavailable**: Service temporarily unavailable

## JSON Response Format

### Success Response
```json
{
  "data": { ... },
  "message": "Optional success message"
}
```

For single resources, return the object directly:
```json
{
  "id": "123",
  "name": "Example",
  "status": "active"
}
```

For collections, return an array:
```json
[
  { "id": "1", "name": "Item 1" },
  { "id": "2", "name": "Item 2" }
]
```

### Error Response
```json
{
  "detail": "Human-readable error message",
  "error": "ERROR_CODE" // optional
}
```

FastAPI automatically formats errors as:
```json
{
  "detail": "Error message"
}
```

## API Endpoint Patterns

### Resource Naming
- Use plural nouns: `/events`, `/users`, `/items`
- Use kebab-case for multi-word resources: `/event-registrations`
- Avoid verbs in URLs (use HTTP methods instead)

### URL Structure
```
GET    /resources          # List all
GET    /resources/{id}     # Get one
POST   /resources          # Create
PUT    /resources/{id}     # Update (full)
PATCH  /resources/{id}     # Update (partial)
DELETE /resources/{id}     # Delete
```

### Query Parameters
- Use for filtering: `GET /events?status=active`
- Use for pagination: `GET /events?page=1&limit=20`
- Use for sorting: `GET /events?sort=date&order=desc`

## Request/Response Headers

### Common Headers
- `Content-Type: application/json` for JSON payloads
- `Accept: application/json` for JSON responses

### CORS Headers (for web access)
```python
allow_origins=["*"]  # Restrict in production
allow_methods=["*"]
allow_headers=["*"]
```

## Input Validation

Use Pydantic models for request validation:
```python
from pydantic import BaseModel, Field

class ResourceCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    status: str = Field(default="active")
```

## Error Handling

Raise HTTPException with appropriate status codes:
```python
from fastapi import HTTPException

# Not found
raise HTTPException(status_code=404, detail="Resource not found")

# Conflict
raise HTTPException(status_code=409, detail="Resource already exists")

# Validation error (handled automatically by Pydantic)
# Returns 422 with validation details
```

## Best Practices for Prototypes

1. **Keep it simple**: Don't over-engineer for scale you don't need yet
2. **Consistent naming**: Use the same patterns across all endpoints
3. **Clear error messages**: Help developers understand what went wrong
4. **Document as you go**: Add docstrings to endpoint functions
5. **Test happy and error paths**: Verify both success and failure cases

## What NOT to Include in Prototypes

These are important for production but can be deferred in prototypes:
- Authentication/Authorization
- Rate limiting
- Request logging/monitoring
- API versioning (unless needed)
- Extensive input sanitization
- Caching strategies
- Pagination for small datasets
