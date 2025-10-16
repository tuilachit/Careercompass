# Career Compass REST API Documentation

## Base URL
```
http://localhost:8000/api/
```

## Authentication
Currently configured for public access. For production, implement proper authentication.

## Endpoints

### Career Paths
**GET** `/api/career-paths/`
- List all career paths
- Query parameters:
  - `category`: Filter by category (technology, healthcare, business, etc.)
  - `education_level`: Filter by education level
  - `growth_outlook`: Filter by growth outlook (high, medium, stable, declining)
  - `work_environment`: Filter by work environment
  - `search`: Search in title, description, and skills
  - `ordering`: Sort by title, created_at, salary_range_min

**GET** `/api/career-paths/{id}/`
- Get specific career path details

**GET** `/api/career-paths/categories/`
- Get all available career categories

**GET** `/api/career-paths/featured/`
- Get featured career paths (random 6)

### Career Assessments
**GET** `/api/assessments/`
- List all available assessments

**GET** `/api/assessments/{id}/`
- Get specific assessment details

**POST** `/api/assessments/{id}/submit/`
- Submit assessment answers
- Body:
  ```json
  {
    "assessment_id": 1,
    "answers": ["option1", "option2", ...],
    "session_id": "optional_session_id"
  }
  ```

### Assessment Results
**GET** `/api/assessment-results/`
- List user's assessment results (requires authentication)
- Query parameter: `session_id` for anonymous users

**GET** `/api/assessment-results/{id}/`
- Get specific assessment result

### Career Resources
**GET** `/api/resources/`
- List career resources (articles, guides, tools)
- Query parameters:
  - `resource_type`: article, guide, tool, video, course, book
  - `category`: resume, interview, networking, skills, job_search, career_planning
  - `difficulty_level`: beginner, intermediate, advanced
  - `is_featured`: true/false
  - `search`: Search in title, content, and tags

**GET** `/api/resources/featured/`
- Get featured resources

**GET** `/api/resources/categories/`
- Get all available resource categories

### User Profiles
**GET** `/api/profiles/me/`
- Get current user's profile (requires authentication)

**PATCH** `/api/profiles/me/`
- Update current user's profile (requires authentication)
- Body:
  ```json
  {
    "career_goals": ["goal1", "goal2"],
    "interests": ["interest1", "interest2"],
    "skills": ["skill1", "skill2"],
    "experience_level": "entry",
    "preferred_work_environment": "office",
    "current_career_path_id": 1
  }
  ```

## Sample Data

The API comes pre-populated with sample data:

### Career Paths (6)
- Software Developer (Technology)
- Data Scientist (Technology)
- UX Designer (Technology)
- Registered Nurse (Healthcare)
- Marketing Manager (Marketing)
- Financial Analyst (Finance)

### Career Assessment (1)
- Career Interest Assessment with 5 questions

### Career Resources (5)
- How to Write a Winning Resume (Featured)
- Interview Preparation Checklist (Featured)
- Building Your Professional Network
- Career Planning Worksheet (Featured)
- Technical Skills Assessment

## Example API Calls

### Get all career paths
```bash
curl http://localhost:8000/api/career-paths/
```

### Get career paths by category
```bash
curl "http://localhost:8000/api/career-paths/?category=technology"
```

### Submit assessment
```bash
curl -X POST http://localhost:8000/api/assessments/1/submit/ \
  -H "Content-Type: application/json" \
  -d '{
    "assessment_id": 1,
    "answers": ["Office setting with regular hours", "Solving complex problems", "Bachelor'\''s degree", ["Programming and coding", "Communication and writing"], "$70,000 - $90,000"]
  }'
```

### Get featured resources
```bash
curl http://localhost:8000/api/resources/featured/
```

## Response Format

All API responses follow this format:

```json
{
  "count": 10,
  "next": "http://localhost:8000/api/career-paths/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Software Developer",
      "description": "Design, develop, and maintain software applications and systems.",
      "category": "technology",
      "salary_range_min": 60000,
      "salary_range_max": 120000,
      "education_level": "bachelors",
      "required_skills": ["Programming", "Problem Solving", "Teamwork"],
      "growth_outlook": "high",
      "work_environment": "office",
      "is_active": true,
      "created_at": "2025-10-16T02:44:43.046294Z",
      "updated_at": "2025-10-16T02:44:43.046294Z"
    }
  ]
}
```

## Admin Interface

Access the admin interface at: http://localhost:8000/admin/
- Username: `admin`
- Password: `admin`

From here you can:
- Manage career paths, assessments, and resources
- View assessment results
- Manage user profiles
- Add new content

## Next Steps for Frontend Integration

1. **Install HTTP client** (axios, fetch, etc.)
2. **Create API service layer** in your Next.js app
3. **Build components** that consume these endpoints
4. **Implement state management** (Redux, Zustand, Context API)
5. **Add error handling** and loading states
6. **Implement authentication** when needed

## Development Notes

- API is currently configured for development with public access
- CORS may need to be configured for frontend integration
- Consider adding API versioning for future updates
- Implement rate limiting for production use
