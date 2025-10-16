@echo off
REM Career Compass Development Startup Script for Windows

echo 🚀 Starting Career Compass Development Environment...

REM Start backend server
echo 📡 Starting Wagtail backend server...
cd backend
call venv\Scripts\activate
start "Wagtail Backend" cmd /k "python manage.py runserver"
cd ..

REM Wait a moment for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend server
echo 🎨 Starting Next.js frontend server...
cd frontend
start "Next.js Frontend" cmd /k "npm run dev"
cd ..

echo.
echo ✅ Development servers are starting!
echo 📡 Backend (Wagtail): http://localhost:8000
echo 🎨 Frontend (Next.js): http://localhost:3000
echo 🔧 Admin Panel: http://localhost:8000/admin
echo.
echo Close the command windows to stop the servers
pause
