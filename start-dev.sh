#!/bin/bash

# Career Compass Development Startup Script

echo "🚀 Starting Career Compass Development Environment..."

# Function to kill background processes on exit
cleanup() {
    echo "🛑 Shutting down servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit
}

# Set up trap to cleanup on script exit
trap cleanup SIGINT SIGTERM EXIT

# Start backend server
echo "📡 Starting Wagtail backend server..."
cd backend
source venv/bin/activate
python manage.py runserver &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 3

# Start frontend server
echo "🎨 Starting Next.js frontend server..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Development servers are running!"
echo "📡 Backend (Wagtail): http://localhost:8000"
echo "🎨 Frontend (Next.js): http://localhost:3000"
echo "🔧 Admin Panel: http://localhost:8000/admin"
echo ""
echo "Press Ctrl+C to stop all servers"

# Wait for user to stop
wait
