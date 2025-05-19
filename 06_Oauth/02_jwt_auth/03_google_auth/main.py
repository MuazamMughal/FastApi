from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.middleware.sessions import SessionMiddleware

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from google.auth.transport import requests as google_requests

import os
import json

app = FastAPI()

# To avoid error: Exception occurred: (insecure_transport) OAuth 2 MUST utilize https.
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Only for testing, remove for production

# Load the secrets file
CLIENT_SECRETS_FILE = "./client_secret.json"
SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
REDIRECT_URI = 'http://localhost:8000/api/google/auth'

FRONTEND_CLIENT_SUCCESS_URI = 'http://localhost:3000/user'
FRONTEND_CLIENT_FAILURE_URI = 'http://localhost:3000'

# SessionMiddleware must be installed to access request.session
app.add_middleware(SessionMiddleware, secret_key="!secret")