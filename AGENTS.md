# AGENTS.md

This file contains guidelines and commands for agentic coding agents working in this repository.

## Project Overview

This is a Flask-based GitHub webhook handler that processes GitHub events (push, pull requests) and stores them in MongoDB. The application uses a modular blueprint architecture.

## Build/Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies (manually based on pip list)
pip install Flask==3.1.2 pymongo==3.12.0 python-dotenv==1.2.1 dnspython==1.16.0
```

### Running the Application
```bash
# Main application (recommended)
python main.py

# Alternative standalone webhook receiver
python webhoook-reciver.py
```

### Testing
```bash
# No formal test framework currently configured
# To run the application manually for testing:
python main.py
# Then test endpoints with curl or Postman
```

### Database Operations
```bash
# MongoDB connection is configured via .env file
# The application automatically connects on startup
# Check database connection in ferret.py
```

## Code Style Guidelines

### Import Organization
- Standard library imports first
- Third-party imports second
- Local application imports last
- Use absolute imports for local modules
- Group related imports together

```python
# Standard library
import os
import json

# Third-party
from flask import Flask, request, Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv

# Local imports
from webhook import webhook_route
from ui import ui_route
```

### Naming Conventions
- **Variables**: snake_case (e.g., `webhook_route`, `repo_name`)
- **Functions**: snake_case (e.g., `create_app`, `git_event_handler`)
- **Classes**: PascalCase (no classes currently in codebase)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MONGODB_URI`)
- **Blueprints**: snake_case with `_route` suffix (e.g., `webhook_route`, `ui_route`)

### Flask Application Structure
- Use application factory pattern (`create_app()`)
- Register blueprints in the factory function
- Keep route definitions in separate blueprint modules
- Use descriptive blueprint names with `_route` suffix

### Error Handling
- Use try-except blocks for database operations
- Validate request headers and content type
- Return appropriate HTTP status codes
- Log errors for debugging (currently using print statements)

### MongoDB Integration
- Use environment variables for connection strings
- Load environment variables with `load_dotenv()`
- Structure database access: client → db → collection
- Handle connection errors gracefully

### JSON Processing
- Use Flask's built-in JSON handling
- Validate JSON content type before processing
- Use `json.dumps()` and `json.loads()` for serialization
- Handle GitHub webhook payload structure carefully

### Environment Configuration
- Use `.env` file for sensitive configuration
- Never commit secrets to version control
- Use `load_dotenv()` at module level
- Provide fallback values where appropriate

## File Structure Conventions

```
/
├── main.py              # Application entry point with factory
├── webhook.py           # Webhook handling blueprint
├── ui.py                # UI routes blueprint
├── ferret.py            # Database connection utilities
├── webhoook-reciver.py  # Standalone webhook receiver (legacy)
├── .env                 # Environment variables (DO NOT COMMIT)
└── .venv/              # Virtual environment
```

## Development Workflow

1. **Feature Development**: Create new functions in appropriate blueprint modules
2. **Database Changes**: Update connection logic in ferret.py if needed
3. **Testing**: Manual testing via `python main.py` and HTTP requests
4. **Environment**: Ensure `.env` file is properly configured

## Common Patterns

### Blueprint Registration
```python
from flask import Flask
from module import blueprint_route

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint_route)
    return app
```

### Database Connection
```python
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongo_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongo_uri)
db = client.database_name
collection = db.collection_name
```

### Webhook Processing
```python
@blueprint_route.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event', 'unknown')
    if request.headers['Content-Type'] == 'application/json':
        payload = request.json
        # Process payload
        return 'OK', 200
```

## Notes for Agents

- The codebase has some duplication (webhook.py vs webhoook-reciver.py)
- Consider consolidating webhook processing logic
- No formal testing framework - recommend adding pytest
- No linting configuration - consider adding flake8/black
- Print statements used for logging - consider proper logging
- Error handling could be more robust
- Type hints are not used but would be beneficial