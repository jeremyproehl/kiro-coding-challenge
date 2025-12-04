---
inclusion: always
---

# Credentials and Secrets Management

## Important Reminder

**ALWAYS prompt the user for credentials when they are needed for deployment or accessing cloud services.**

## When to Prompt for Credentials

Prompt the user to provide credentials when:

1. **Deploying to AWS**: Ask for AWS credentials (Access Key ID, Secret Access Key, Session Token if using temporary credentials)
2. **Accessing cloud resources**: Any operation that requires authentication
3. **Running deployment scripts**: Before executing scripts that interact with cloud providers
4. **Testing deployed APIs**: If authentication is required

## How to Handle Credentials

### DO:
- ✅ Ask the user to provide credentials explicitly
- ✅ Store credentials in environment variables or `.env` files (add to `.gitignore`)
- ✅ Use the user's existing AWS CLI configuration when available
- ✅ Remind users that credentials are sensitive and should not be committed to git

### DON'T:
- ❌ Never hardcode credentials in source code
- ❌ Never commit credentials to version control
- ❌ Never assume credentials are available without asking
- ❌ Never expose credentials in logs or error messages

## Example Prompts

When deployment is needed:
```
"To deploy to AWS, I'll need your AWS credentials. Please provide:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_SESSION_TOKEN (if using temporary credentials)
- AWS_DEFAULT_REGION

You can also configure these using 'aws configure' if you have the AWS CLI installed."
```

When credentials are missing:
```
"I don't have AWS credentials configured. Would you like to:
1. Provide credentials now
2. Use your existing AWS CLI configuration
3. Set up credentials in a .env file"
```

## Credential Storage Patterns

### Environment Variables
```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_SESSION_TOKEN="..."
export AWS_DEFAULT_REGION="us-west-2"
```

### .env File (for local development)
```
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_SESSION_TOKEN=...
AWS_DEFAULT_REGION=us-west-2
```

### AWS CLI Configuration
```bash
aws configure
# Or use profiles
aws configure --profile myprofile
```

## Security Reminders

- Credentials should be treated as highly sensitive
- Temporary credentials (with session tokens) are preferred over long-term credentials
- Always add `.env` files to `.gitignore`
- Rotate credentials regularly
- Use IAM roles when running in AWS environments (Lambda, EC2, etc.)
