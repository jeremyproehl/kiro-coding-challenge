# Steering Files

This directory contains steering files that provide context and guidelines to Kiro when working on this project.

## Active Steering Files

### 1. api-standards.md
**Inclusion**: Conditional (file match)
**Pattern**: `**/*api*.py|**/main.py|**/*endpoint*.py|**/*route*.py`

Provides REST API conventions for prototype applications including:
- HTTP methods and their semantic meanings
- Standard HTTP status codes
- JSON response format standards
- API endpoint patterns and naming conventions
- Input validation with Pydantic
- Error handling best practices

This file is automatically included when working with API-related Python files.

### 2. credentials.md
**Inclusion**: Always

Reminds Kiro to:
- Always prompt for credentials when needed for deployment
- Never hardcode credentials in source code
- Use environment variables or .env files for credential storage
- Follow security best practices for credential management

This file is always active to ensure credentials are handled securely.

### 3. check-documentation.md
**Inclusion**: Always

Reminds Kiro to:
- Check official documentation before implementing features
- Search for current best practices and examples
- Verify syntax for library versions (especially Pydantic v2 changes)
- Use MCP tools to search AWS documentation
- Look up CDK patterns and Lambda bundling strategies

This file is always active to encourage documentation-driven development.

## How Steering Files Work

- **Always included**: Files with `inclusion: always` are included in every interaction
- **Conditionally included**: Files with `inclusion: fileMatch` are included when the file pattern matches
- **Manual inclusion**: Files can be referenced manually using `#` in chat

## Modifying Steering Files

To add or update steering files:
1. Create a new `.md` file in this directory
2. Add front matter with inclusion rules:
   ```yaml
   ---
   inclusion: always
   ---
   ```
   or
   ```yaml
   ---
   inclusion: fileMatch
   fileMatchPattern: '**/*.py'
   ---
   ```
3. Write your guidelines in Markdown format

## Best Practices

- Keep steering files focused on specific topics
- Use clear, actionable guidance
- Include examples where helpful
- Update regularly as project standards evolve
- Don't duplicate information across files
