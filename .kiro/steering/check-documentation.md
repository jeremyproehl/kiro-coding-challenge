---
inclusion: always
---

# Documentation and Context Checking

## Critical Reminder

**ALWAYS check official documentation and context when working with Python, AWS CDK, or AWS services.**

## When to Check Documentation

You should search documentation in these situations:

### Python Libraries
- **FastAPI**: When creating or modifying API endpoints, middleware, or request/response handling
- **Pydantic**: When defining models, validators, or using field constraints
  - ⚠️ **Important**: Pydantic v2 changed `regex` to `pattern` in field validators
- **Boto3**: When interacting with AWS services from Python code
- **Any third-party library**: Before using features you're not 100% certain about

### AWS CDK
- **CDK Constructs**: When defining infrastructure resources
- **Lambda Functions**: Especially for Python Lambda dependency bundling
  - 🔑 **Key Resource**: `@aws-cdk/aws-lambda-python-alpha` for Python Lambda functions
  - Use `PythonFunction` construct for automatic dependency management
- **API Gateway**: When configuring REST APIs, CORS, or integrations
- **DynamoDB**: When defining tables, indexes, or access patterns

### AWS Services
- **Service Limits**: Before designing solutions
- **Regional Availability**: When deploying to specific regions
- **Best Practices**: For architecture and implementation patterns

## How to Check Documentation

### Use MCP Tools
```
Use the aws_search_documentation tool with appropriate topics:
- "cdk_docs" for CDK concepts and APIs
- "cdk_constructs" for CDK code examples and patterns
- "reference_documentation" for API/SDK references
- "general" for architecture and best practices
```

### Search Patterns
1. **Before implementing**: Search for examples and best practices
2. **When stuck**: Look for troubleshooting guides
3. **After errors**: Search for the specific error message
4. **For new features**: Check "current_awareness" topic for recent updates

## Common Documentation Needs

### Python Lambda Dependency Bundling
**Always check**: How to properly bundle Python dependencies for Lambda
- Docker-based bundling (requires Docker)
- Local bundling with platform-specific wheels
- Using Lambda layers
- The `@aws-cdk/aws-lambda-python-alpha` module

### Pydantic Version Differences
**Always verify**: Pydantic syntax for the version you're using
- v1 vs v2 differences
- Field validators: `regex` (v1) vs `pattern` (v2)
- Model configuration changes

### DynamoDB Reserved Keywords
**Always check**: If attribute names are reserved keywords
- Common ones: `status`, `capacity`, `name`, `date`, `location`
- Use `ExpressionAttributeNames` to handle reserved keywords

### CDK Best Practices
**Always review**: 
- Construct patterns for the service you're using
- How to properly configure IAM permissions
- Asset bundling strategies

## Documentation Search Examples

### Good Searches
```
"PythonFunction aws-lambda-python-alpha CDK Python dependencies"
"Pydantic field validators pattern regex v2"
"DynamoDB reserved keywords ExpressionAttributeNames boto3"
"FastAPI CORS middleware configuration"
"CDK Lambda function environment variables"
```

### When to Search
- ❓ "I'm not sure if this is the right approach" → Search first
- ⚠️ "This might have changed in recent versions" → Check current_awareness
- 🐛 "Getting an unexpected error" → Search for the error message
- 📚 "Need to implement something new" → Look for examples first

## Benefits of Checking Documentation

1. **Avoid deprecated patterns**: Stay current with latest best practices
2. **Prevent common mistakes**: Learn from documented pitfalls
3. **Save time**: Find working examples instead of trial and error
4. **Better solutions**: Discover features you didn't know existed
5. **Version compatibility**: Ensure code works with current library versions

## Remember

> "When in doubt, search it out. Documentation is your friend, not a last resort."

The few minutes spent checking documentation can save hours of debugging and refactoring.
