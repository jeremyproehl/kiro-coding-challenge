# API Documentation

This folder contains auto-generated API documentation created with `pdoc`.

## Viewing the Documentation

Open `index.html` in your web browser to view the complete API documentation.

## Regenerating Documentation

To regenerate the documentation after code changes:

```bash
cd backend
python3 -m pdoc main -o docs
```

## Contents

- `index.html` - Main documentation index
- `main.html` - Detailed module documentation
- `search.js` - Search functionality

The documentation includes:
- All API endpoints with descriptions
- Pydantic model schemas
- Function signatures and parameters
- Return types and exceptions
