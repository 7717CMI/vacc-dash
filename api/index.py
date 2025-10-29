"""
Vercel serverless function handler for Dash app
This file is required for Vercel to properly deploy the Dash application
"""
import sys
import os

# Add the parent directory to the path so we can import app
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Change working directory to parent for asset resolution
os.chdir(parent_dir)

try:
    # Import the Flask server from app
    from app import server
    
    # Vercel expects the WSGI application to be exported as 'handler'
    # The @vercel/python builder will automatically wrap this for serverless execution
    handler = server
    
except ImportError as e:
    # Fallback: try importing app directly
    import app
    handler = app.server
except Exception as e:
    # If all else fails, provide a minimal error handler
    from flask import Flask
    error_app = Flask(__name__)
    
    @error_app.route('/', defaults={'path': ''})
    @error_app.route('/<path:path>')
    def catch_all(path):
        return f"""
        <html>
            <head><title>Application Error</title></head>
            <body>
                <h1>Application Error</h1>
                <p>Failed to load Dash application.</p>
                <p>Error: {str(e)}</p>
                <p>Please check Vercel logs for more details.</p>
            </body>
        </html>
        """, 500
    
    handler = error_app

