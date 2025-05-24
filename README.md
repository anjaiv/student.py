# Student Microservice API

This is a simple Flask-based microservice that manages a list of students.

## Endpoints

- `GET /students` – List all students
- `GET /students/<id>` – Get student by ID
- `POST /students` – Add a new student (with JSON body)

## Example JSON for POST

```json
{
  "id": 3,
  "name": "Elena",
  "grade": 10
}
