"""
Vercel serverless function handler for Dash app
This file is required for Vercel to properly deploy the Dash application
"""
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel expects a handler function that works with Flask WSGI
# Export the Flask server for Vercel
handler = app.server

