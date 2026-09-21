import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task


@csrf_exempt
def home(request):

    if request.method == "GET":
        tasks = Task.objects.all()

        task_data = []

        for task in tasks:
            task_data.append({
                "id": task.id,
                "task_name": task.task_name,
                "description": task.description,
                "status": task.status,
                "created_date": task.created_date
            })

        return JsonResponse({
            "message": "Tasks retrieved successfully",
            "tasks": task_data
        })

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            task = Task.objects.create(
                task_name=data.get("task_name", ""),
                description=data.get("description", ""),
                status=data.get("status", "Pending")
            )

            return JsonResponse({
                "message": "Task added successfully",
                "task": {
                    "id": task.id,
                    "task_name": task.task_name,
                    "description": task.description,
                    "status": task.status,
                    "created_date": task.created_date
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON data"
            }, status=400)

    if request.method == "PUT":
        try:
            data = json.loads(request.body)

            task_id = data.get("id")
            task = Task.objects.get(id=task_id)

            task.task_name = data.get("task_name", task.task_name)
            task.description = data.get("description", task.description)
            task.status = data.get("status", task.status)
            task.save()

            return JsonResponse({
                "message": "Task updated successfully",
                "task": {
                    "id": task.id,
                    "task_name": task.task_name,
                    "description": task.description,
                    "status": task.status,
                    "created_date": task.created_date
                }
            })

        except Task.DoesNotExist:
            return JsonResponse({
                "error": "Task not found"
            }, status=404)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON data"
            }, status=400)

    if request.method == "DELETE":
        try:
            data = json.loads(request.body)

            task_id = data.get("id")
            task = Task.objects.get(id=task_id)
            task.delete()

            return JsonResponse({
                "message": "Task deleted successfully"
            })

        except Task.DoesNotExist:
            return JsonResponse({
                "error": "Task not found"
            }, status=404)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON data"
            }, status=400)

    return JsonResponse({
        "message": "Method not supported",
        "method": request.method
    }, status=405)