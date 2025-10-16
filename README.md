# Career Compass

A modern career guidance application built with Wagtail CMS backend and Next.js frontend.

## 🚀 Tech Stack

### Backend
- **Wagtail CMS** - Django-based content management system
- **Django REST Framework** - API endpoints
- **Wagtail Grapple** - GraphQL API for headless CMS
- **PostgreSQL** (ready for production) / SQLite (development)
- **Python 3.13**

### Frontend
- **Next.js 15** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **Next SEO** - SEO optimization

## 📁 Project Structure

```
career-compass/
├── backend/                 # Wagtail CMS backend
│   ├── core/               # Django project settings
│   ├── home/               # Home app with page models
│   ├── search/             # Search functionality
│   ├── venv/               # Python virtual environment
│   ├── manage.py           # Django management script
│   └── requirements.txt    # Python dependencies
├── frontend/               # Next.js frontend
│   ├── app/                # Next.js App Router
│   ├── public/             # Static assets
│   ├── package.json        # Node.js dependencies
│   └── .env.local          # Environment variables
└── README.md               # This file
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.13+
- Node.js 18+
- Git

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Activate virtual environment:**
   ```bash
   source venv/bin/activate  # macOS/Linux
   # or
   .\venv\Scripts\activate   # Windows
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```
   Default credentials: `admin` / `admin`

5. **Start development server:**
   ```bash
   python manage.py runserver
   ```
   Backend will be available at: http://localhost:8000
   Admin panel: http://localhost:8000/admin

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```
   Frontend will be available at: http://localhost:3000

## 🔧 Configuration

### Environment Variables

The frontend is configured to connect to the backend API via:
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api/
```

### API Endpoints

- **Wagtail Admin:** http://localhost:8000/admin
- **GraphQL API:** http://localhost:8000/graphql/
- **REST API:** http://localhost:8000/api/

## 🚀 Development

### Backend Development
- Use Wagtail's admin interface to create and manage content
- Create custom page models in the `home` app
- Add new apps for specific functionality
- Use GraphQL for headless content delivery

### Frontend Development
- Use Next.js App Router for page routing
- Leverage Tailwind CSS for styling
- Implement animations with Framer Motion
- Connect to backend via GraphQL or REST API

## 📝 Features

- ✅ **Content Management** - Full Wagtail CMS with admin interface
- ✅ **Headless API** - GraphQL and REST API endpoints
- ✅ **Modern Frontend** - Next.js with TypeScript and Tailwind
- ✅ **Responsive Design** - Mobile-first approach
- ✅ **SEO Ready** - Next SEO integration
- ✅ **Animation Support** - Framer Motion integration

## 🔮 Future Enhancements

- User authentication and profiles
- Career assessment tools
- Job matching algorithms
- Resume builder
- Interview preparation tools
- Networking features
- Analytics dashboard

## 📚 Documentation

- [Wagtail Documentation](https://docs.wagtail.org/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Framer Motion Documentation](https://www.framer.com/motion/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

**Happy coding! 🎉**
