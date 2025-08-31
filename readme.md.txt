# Think Wealth Python Backend

Backend service for Think Wealth app.  
Runs FastAPI with Pandas, pandas-ta, and vectorbt.

## Run locally (optional for testing)
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

Then visit http://127.0.0.1:8000/

## Deploy on Render
1. Push this repo to GitHub.
2. On Render, create a new "Web Service".
3. Build Command: pip install -r requirements.txt
4. Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
5. Render will give you a public URL like:
   https://thinkwealth-backend.onrender.com
