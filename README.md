# GitHub Webhook Dashboard

A Flask application that processes GitHub webhooks and displays events in a web dashboard.
![screen shot of the page](https://github.com/softCub/webhook-repo/blob/main/ss.png)
Frontend is opencode

## What It Does

- Receives and processes GitHub webhook events (push and pull requests)
- Stores event data in MongoDB database
- Displays events in a web dashboard with most recent events first
- Provides API endpoints for accessing event data
- Shows event badges (push, pull_req, merged) with color-coded display

## Installation Steps

1. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

2. Install required dependencies:
   ```bash
   pip install Flask==3.1.2 pymongo==3.12.0 python-dotenv==1.2.1 dnspython==1.16.0
   ```

3. Set up environment variables (see Environment Variables section below)

4. Run the application:
   ```bash
   python main.py
   ```

## Environment Variables

Create a `.env` file in the project root with the following variable:

- `MONGODB_URI` - MongoDB connection string (required)
  
Example:
```
MONGODB_URI="mongodb+srv://username:password@cluster.mongodb.net/database_name"
```

## Usage

### Web Dashboard
I am using ngrok for port forwarding
Access the main dashboard at:
```
http://localhost:5000
https://lavone-ironfisted-noncausatively.ngrok-free.dev
```

### Webhook Endpoint
Send GitHub webhooks to:
```
POST http://localhost:5000/webhook
https://lavone-ironfisted-noncausatively.ngrok-free.dev/webhook
```



### Event Types Supported
- **push**: Code push events with repository and author information
- **pull_request**: Pull request events with branch information
- **merged**: Merged pull request events

The dashboard displays events in reverse chronological order (most recent first) with appropriate badges and styling for each event type.
