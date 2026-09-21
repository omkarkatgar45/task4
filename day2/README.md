# Week 4 - Day 2

## Django Models and Database

### Topics Learned

1. Django Models
2. Django Fields
3. SQLite Database
4. Migrations
5. Django Admin Panel
6. Creating a Superuser

### Task Model

A `Task` model was created with the following fields:

- `title` - Task title
- `description` - Task description
- `completed` - Task completion status
- `created_at` - Task creation date and time

### Model Code

```python
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
