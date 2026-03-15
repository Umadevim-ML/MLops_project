#!/bin/bash

echo "Starting FastAPI..."

cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 &

cd ..

echo "Starting Streamlit..."

streamlit run frontend/app.py \
--server.port $PORT \
--server.address 0.0.0.0 \
--server.headless true